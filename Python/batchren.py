import glob
import os
import platform
(PATH_SEPERATOR, PARAM_SEPERATOR) = ("/" if platform.system().lower() != "windows" else "\\", "-->")
(code_length, code_app_end, code_append_start, code_substitute) = (4, '-app', 'app-', 'subs')
# modes: replace, append in start, append in end,
# append both, remove part, change type, numberify(start or end), srt sync
sourcePath = input('Directory: ')
statement = input('Statement: ')
[code, text] = [statement[: code_length], statement[code_length + 1:]]

# renameType = input('Rename Type: ')
# mode = selectMode(renameType.split())
items = 0
print('logs:')
for file in glob.glob(sourcePath + f'{PATH_SEPERATOR}*.*'):
    i = 1
    newFileName = file
    if code == code_app_end:
        while i <= len(file) and file[-i] != '.':
            i += 1
        newFileName = file[:-i] + text + file[-i:]
    elif code == code_append_start:
        while i <= len(file) and file[-i] != PATH_SEPERATOR:
            i += 1
        i -= 1
        newFileName = file[:-i] + text + file[-i:]
    elif code == code_substitute:
        # in future, handle texts with space between them
        [old, new] = text.split(PARAM_SEPERATOR)
        while i <= len(file) and file[-i] != PATH_SEPERATOR:
            i += 1
        i -= 1
        shortName = file[-i:]
        shortName = shortName.replace(old, new)
        newFileName = file[:-i] + shortName

    if newFileName != file:
        items += 1
        os.rename(file, newFileName)
        print('\t%3d) \'%s\'\t----------->\t\'%s\'' % (items, file, newFileName))
    # renameType = renameType.replace('_XXX_', sourcePath)

print(str(items) + ' file(s) has been renamed.')
