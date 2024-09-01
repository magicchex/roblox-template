local Players = game:GetService('Players')
local Camera = game.Workspace:FindFirstChildOfClass('Camera')
Camera.CameraType = Enum.CameraType.Scriptable
Camera.CFrame = CFrame.new(Vector3.new(20.265, 7.328, -16.8)) * CFrame.Angles(0, 90, 0)

function setup(player: Player)
	local player = player.Character
end
Players.PlayerAdded:Connect(setup)
print("Test the workflows: attempt 5")