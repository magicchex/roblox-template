local process = require('@lune/process')
local fs = require('@lune/fs')

local function main()
	local buildFilePath = string.format('%s/%s.%s', process.args[1], process.args[2], process.args[3])
	print(string.format('Running rojo build -o %s', buildFilePath))
	pcall(fs.writeDir, process.args[1])
	local result = process.exec('rojo', { 'build', '-o', buildFilePath })
	print(result.ok and 'Build execution was successful!' or 'Build execution failed!')
	print(
		string.format(
			'Traceback:\n%s',
			result.ok and result.stdout or string.format('%s\n%s', result.stderr, result.stdout)
		)
	)
end
return main
