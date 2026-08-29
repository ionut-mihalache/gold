cmake_minimum_required(VERSION 3.20)

project(GOLD LANGUAGES NONE)

find_package(Java REQUIRED COMPONENTS Runtime)
find_package(Python3 REQUIRED COMPONENTS Interpreter)

set(ANTLR_VERSION "4.13.0")
set(ANTLR_JAR "${CMAKE_SOURCE_DIR}/antlr/antlr-${ANTLR_VERSION}-complete.jar")

set(GRAMMARS_DIR "${CMAKE_SOURCE_DIR}/grammars")

set(GRAMMARS_OUTPUT_DIR "${CMAKE_SOURCE_DIR}/grammars/gen")

set(DESCRIPTIONS_DIR "${CMAKE_SOURCE_DIR}/descriptions")

set(LEXER_GRAMMAR "${GRAMMARS_DIR}/GOLDLexer.g4")

set(PARSER_GRAMMAR "${GRAMMARS_DIR}/GOLDParser.g4")

if(NOT EXISTS "${ANTLR_JAR}")
    message(FATAL_ERROR "ANTLR JAR not found: ${ANTLR_JAR}")
endif()

if(NOT EXISTS "${LEXER_GRAMMAR}")
    message(FATAL_ERROR "Lexer grammar not found: ${LEXER_GRAMMAR}")
endif()

if(NOT EXISTS "${PARSER_GRAMMAR}")
    message(FATAL_ERROR "Parser grammar not found: ${PARSER_GRAMMAR}")
endif()


set(ANTLR_OPTIONS "-Dlanguage=Python3" "-visitor" "-no-listener" "-Xexact-output-dir")

set(LEXER_OUTPUT "${GRAMMARS_OUTPUT_DIR}/GOLDLexer.py")
set(PARSER_OUTPUT "${GRAMMARS_OUTPUT_DIR}/GOLDParser.py")

add_custom_command(
    OUTPUT ${LEXER_OUTPUT}

    COMMAND ${CMAKE_COMMAND} -E make_directory "${GRAMMARS_OUTPUT_DIR}"

    COMMAND "${Java_JAVA_EXECUTABLE}" -jar "${ANTLR_JAR}" ${ANTLR_OPTIONS} "${LEXER_GRAMMAR}" -o "${GRAMMARS_OUTPUT_DIR}"

    DEPENDS "${LEXER_GRAMMAR}" "${ANTLR_JAR}"

    COMMENT "Generating Python lexer with ANTLR" VERBATIM
)

add_custom_command(
    OUTPUT ${PARSER_OUTPUT}

    COMMAND ${CMAKE_COMMAND} -E make_directory "${GRAMMARS_OUTPUT_DIR}"

    COMMAND "${Java_JAVA_EXECUTABLE}" -jar "${ANTLR_JAR}" ${ANTLR_OPTIONS} "${PARSER_GRAMMAR}" -lib "${GRAMMARS_OUTPUT_DIR}" -o "${GRAMMARS_OUTPUT_DIR}"

    DEPENDS "${PARSER_GRAMMAR}" "${LEXER_OUTPUT}" "${ANTLR_JAR}"

    COMMENT "Generating Python parser with ANTLR" VERBATIM
)

add_custom_target(generate
    DEPENDS ${LEXER_OUTPUT} ${PARSER_OUTPUT}
)

file(GLOB DESCRIPTION_FILES
    "${DESCRIPTIONS_DIR}/*.gold"
)

set(DESCRIPTION_ARGS)

foreach(FILE ${DESCRIPTION_FILES})
    file(RELATIVE_PATH RELATIVE_FILE
        "${DESCRIPTIONS_DIR}"
        "${FILE}"
    )

    list(APPEND DESCRIPTION_ARGS "${RELATIVE_FILE}")
endforeach()

add_custom_target(run
    DEPENDS generate

    COMMAND "${CMAKE_COMMAND}" -E env
            "PYTHONPATH=${CMAKE_SOURCE_DIR}"
            "${Python3_EXECUTABLE}"
            "${CMAKE_SOURCE_DIR}/gold.py"
            ${DESCRIPTION_ARGS}

    WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"

    USES_TERMINAL
)

add_custom_target(clean-generated
    COMMAND "${CMAKE_COMMAND}" -E remove_directory "${GRAMMARS_OUTPUT_DIR}"

    COMMENT "Removing generated ANTLR files" VERBATIM
)
