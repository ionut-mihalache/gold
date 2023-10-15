# General Objects Language Description #

**General Objects Language Description** (*__GOLD__*) is a **describing** language that can be used to describe common patterns 
in applications that are implemented using multiple programming languages (e.g. frontend - backend for web application).

## Language properties and description ##
The main component of the language is the __block__ or __object__ and the main action is the __description__.

The current version of the __GOLD__ language defines the following blocks that can be used for description:
* __description__: the main block of the language. It contains all the other blocks of the language.
* __header__: this block is part of the __description__ block. It is used to describe the necessary information for each language.
* __body__: this block is part of the __description__ block. It is used to describe the common parts of code of different languages.
* __language__: this block is part of the __header__ block. It is used to describe the files for a specific language and the specific type of that language.
* __files__: this block is part of the __language__ block. It is used to describe all the files paths for a language, as well as the start and the end for inserting the __body__ block contents.
* __types__: this block is part of the __language__ block. It is used to describe the common __GOLD__ types using language specific types.

### *GOLD* blocks details ###

The __description__ is the most important block of the *__GOLD__* language, it contains all the other blocks and a *__GOLD__* file can have multiple __description__ blocks.

The __header__ block is part of the __description__ block and it contains all the __language__ blocks necessary. Only one __header__ block is allowed for each __description__ block.

The __language__ block describes the properties for each supported language. It contains one __files__ block and one __types__ block.

The __files__ block describes the necessary information for generating the appropriate code for the supported language. The information is comprised by the following:
1. path to the language specific file
2. a tag for marking the start of the __description__ block
3. a tag for marking the end of the __description__ block

The tags for marking the start and the end of the __description__ block in the file __should__ be a new separte line in the file (usually contained in a comment for each specific language).

The __types__ block describes the mapping between a __GOLD__ specific type and the language specific type. Each __types__ block has to describe the same __GOLD__ specific types for all the languages in order to make it possible to use the types in the __body__ block.

The __body__ block describes the common parts of all the languages described by the __language__ blocks inside the __header__ block. The sintax is similar to any other language in order to make it easy to write and understand.
The type will be replaced accordingly for each __language__ block described by the __header__ block.

For the current version a __GOLD__ file looks like this:
```
% GOLD comment - it is ignored on code generation %
description __description_block_name__ {
    header {
        % Multiple language block can be described %
        language __supported_lang__ {
            files {
                [
                    "__path_to_file_for_supported_lang__",
                    __start_of_the_descrition_block__,
                    __end_of_the_description_block__
                ];
            };

            % Multiple type can be defined %
            types {
                __new_gold_type__ = t<__supported_lang_specific_type__>;
            };
        };
    };

    % The common code is described inside the body block %
    body {
        __new_gold_type__ __name__ = v<__value_for_the_name_var__>;
    };
};
```
The current common patterns supported are focused on common constants that are needed in different programming languages.
The supported programming languages are *PHP* and *Javascript*.
