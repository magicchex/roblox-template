local process = require('@lune/process')
local fs = require('@lune/fs')
local c = require('../configuration').process

local function main()
	local buildFilePath = string.format('%s/%s.%s', c.outFolder, c.placeFileName, c.placeFileExtension)
	print(string.format('Running rojo build -o %s', buildFilePath))
	pcall(fs.writeDir, c.outFolder)
	local result = process.spawn('rojo', { 'build', '-o', buildFilePath })

	print(result.ok and 'Build execution was successful!' or 'Build execution failed!')
	print(
		string.format(
			'Traceback:\n%s',
			result.ok and result.stdout or string.format('%s\n%s', result.stderr, result.stdout)
		)
	)
end
return main
