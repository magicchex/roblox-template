local process = require('@lune/process')
local fsPlus = require('./lib/fsPlus')
local stdio = require('@lune/stdio')
local config = require('./config').BulkUploadPlace

-- MARK: WIP
print('Not implemented!')
return

-- local PUBLISHING_KEY = process.args[1]
-- local UNIVERSE_ID = process.args[2]
-- local PLACE_DIRECTORY = process.args[3]

-- if not (PUBLISHING_KEY and UNIVERSE_ID and PLACE_DIRECTORY) then
-- 	print('BulkUploadPlace.luau requires three arguments!')
-- 	return
-- end
-- function runRBXCloud(
-- 	filepath: string,
-- 	placeId: number | string,
-- 	universeId: string,
-- 	versionType: 'saved' | 'published',
-- 	apiKey: string
-- )
-- 	return process.exec('rbxcloud', {
-- 		string.format(
-- 			'experience publish --filename %s --place-id %s --universe-id %s --version-type %s --api-key %s',
-- 			filepath,
-- 			tostring(placeId),
-- 			universeId,
-- 			versionType,
-- 			apiKey
-- 		),
-- 	})
-- end
-- for _, path in ipairs(fsPlus.super.readDir(PLACE_DIRECTORY)) do
-- 	if fsPlus.super.isFile(path) then
-- 		local filename = fsPlus.getFullFilename(path)
-- 		print(filename)
-- 		if string.find(filename, 'rbxl') or string.find(filename, 'rbxlx') then
-- 			local place_id: number? = config.filePlaceIdMap[filename]
-- 			local program
-- 			if place_id then
-- 				program = runRBXCloud(path, place_id, UNIVERSE_ID, 'saved', PUBLISHING_KEY)
-- 			else
-- 				program = runRBXCloud(
-- 					path,
-- 					stdio.prompt(
-- 						'select',
-- 						string.format(
-- 							'[BulkUploadPlace] Couldn\'t find Place ID for file: "%s"\n[BulkUploadPlace] Awaiting for Place ID to associate...\n',
-- 							filename
-- 						)
-- 					),
-- 					UNIVERSE_ID,
-- 					'saved',
-- 					PUBLISHING_KEY
-- 				)
-- 			end
-- 			print('Traceback:')
-- 			print(program.stdout)
-- 		end
-- 	end
-- end
