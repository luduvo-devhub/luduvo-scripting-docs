--[[
	Environment Dumper
	
	by lua_u (i know my name is stupid)
--]]

local Environment = getmetatable(getfenv()).__index

local function Handle(Tab: {}, Depth: number)
	local Stuff = ""
	for Name, Value in pairs(Tab) do
		if Value == Tab then
			continue -- no incurse
		end
		local Line = table.concat(table.create(Depth, "\t"), "") .. `[{Name}] = `
		if typeof(Value) == "table" then
			Line ..= "{\n" .. Handle(Value, Depth + 1) .. "}"
		else
			Line ..= typeof(Value)
		end
		
		Stuff ..= Line .. "\n"
	end
	
	return Stuff
end

print(Handle(Environment, 2))