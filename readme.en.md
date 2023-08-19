# Version 1.0.8

## What have I done in the new version?
- Type optimization, static type declaration for some variables/parameters
- Encapsulate some basic classes, adopt declarative style, and make the structure as clear and searchable as possible
- Renamed some variables to express "what" more clearly
- Added/deleted some functions (will be mentioned below)

## New function
- setCard(self, **kwargs): Allow users to customize the content of the card in the settings (because considering that it may be used as a description of personal software, documents, etc., the foregoing, etc.), kwarg is a parameter in ReLabel

## Main naming changes

### Global
- total_lay -> _globalLay

### Left Zone
- left_lay -> _leftLay
- left_line_lay -> _runAndSet
- homepageLine -> _statusLay
- left_listBox -> listBox

### Central District
- mid_spliter -> midSplitter

### Right Area
- right_lay -> _rightLay
- homepageLay -> _homepageLay
- right_tutorial_group -> remakerGroup
- right_editor -> codesViewer
- right_tutorial -> remarker
- group_lay -> _groupLay
- title_show -> codeTitle
- right_temp_widget_hp -> _showHomePage
- right_temp_widget_org -> _showCodes

Note: The 1.0.8 version is in a hurry, and some content has been temporarily adjusted, but the overall function can be said to be basically unchanged. However, the time has been rushed recently, and the rest needs to be reserved for future development; in addition, 1.0.8 The version is only a preview version, and does not support functions such as creation
> Features that may appear in the future
> - Generate PDF from the command line
> - call pyinstaller faster packaging command line
> - Fully optimized listBox
> - Initial loading performance optimization
> - "I can't do more, but I must follow my original intention..." ——2023.8, 19
