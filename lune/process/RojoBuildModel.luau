local fs = require('@lune/fs')
local roblox = require('@lune/roblox')
local c = require('../configuration').process
local function main()
	print(fs.isDir(c.sourceFolder) and 'Found source folder' or 'Could not find source folder!')
	if not fs.isDir(c.sourceFolder) then
		return
	end
	print(fs.readDir(c.sourceFolder))
end

return main
