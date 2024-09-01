for _, item: BasePart in ipairs(game.Workspace:GetDescendants()) do
	if item:IsA('Part') then
		item.CastShadow = false
		item.Anchored = true
	end
end
