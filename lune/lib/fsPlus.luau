local super = require('@lune/fs')
local process = require('@lune/process')
local fsPlus = {}
fsPlus.super = super
fsPlus.sep = process.os == 'windows' and '\\' or '/'
function fsPlus.getDepth(path: string): number
	return #string.split(path, fsPlus.sep) - (#string.split(path, '..') - 1)
end

function fsPlus.convertPath(path: string, alwaysConvertToOs: true?): string
	local result = path
	local unixIdx = string.find(result, '/')
	local windowIdx = string.find(result, '\\')
	if alwaysConvertToOs then
		if fsPlus.sep == '/' then
			return string.gsub(path, '\\', '/')
		else
			return string.gsub(path, '/', '\\')
		end
	end

	if unixIdx and windowIdx then
		if unixIdx < windowIdx then
			return string.gsub(path, '\\', '/')
		else
			return string.gsub(path, '/', '\\')
		end
	end
	if unixIdx then
		return string.gsub(path, '/', '\\')
	end
	if windowIdx then
		return string.gsub(path, '\\', '/')
	end
	return result
end

function fsPlus.insertToFile(filepath: string, idx: number, content: string): boolean
	local success, fileContents, _
	success, fileContents = pcall(super.readFile, filepath)
	if success then
		success, _ = pcall(
			super.writeFile(
				filepath,
				string.format(
					'%s%s%s',
					fileContents:sub(1, idx),
					content,
					(idx == #fileContents or idx == -1) and '' or fileContents:sub(idx + 1)
				)
			)
		)
	end
	return success
end
function fsPlus.appendToFile(filepath: string, content: string): boolean
	return fsPlus.insertToFile(filepath, -1, content)
end
function fsPlus.getExtension(path: string): string
	if super.isFile(path) then
		local startIndex, _ = string.find(path, '.', -1, true)
		if startIndex then
			return string.sub(path, startIndex)
		end
	end
	return ''
end
function fsPlus.getFilename(path: string): string
	if super.isFile(path) then
		local startIndex, _ = string.find(path, '.', -1, true)
		if startIndex then
			return string.sub(path, 1, startIndex - 1)
		end
	end
	return ''
end
function fsPlus.getFullFilename(path: string): string
	local filename = fsPlus.getFilename(path)
	local extension = fsPlus.getExtension(path)
	return filename .. extension
end
return fsPlus
