# Language Independent Describing Expression #

**General Objects Language Description** (*__GOLD__*) is a **describing** language that can be used to describe common patterns 
in applications that are implemented using multiple programming languages (e.g. frontend - backend for web application).

## Language properties and description - TODO ##
The main component of the language is the __block__ or __object__ and the main action is the __description__.

The current version of the __GOLD__ language defines the following blocks that can be used for description:
* __description__: the main block of the language. It contains all the other blocks of the language.
* __header__: this block is part of the __description__ block. It is used to describe the necessary information for each language.
* __body__: this block is part of the __description__ block. It is used to describe the common parts of code of different languages.
* __language__: this block is part of the __header__ block. It is used to describe the files for a specific language and the specific type of that language.
* __files__: this block is part of the __language__ block. It is used to describe all the files paths for a language, as well as the start and the end for inserting the __body__ block contents.
* __types__: this block is part of the __language__ block. It is used to describe the common __GOLD__ types using language specific types.

For the current version a __GOLD__ file looks like this:
```
% GOLD comment - it is ignored on code generation %
description __description_block_name__ {
    header {
        % Multiple language block can be described %
        language __lang_name__ {
            files {
                [
                    "__path_to_file_for_lang_name__",
                    __start_of_the_descrition_block__,
                    __end_of_the_description_block__
                ];
            };

            % Multiple type can be defined %
            types {
                __new_gold_type__ = t<__lang_name_specific_type__>;
            };
        };
    };

    % The common code is described inside the body block %
    body {
        __new_gold_type__ __name__ = v<__value_for_the_name_var__>;
    };
};
```
