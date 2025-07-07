-- Load the addon DB
if not CraterBaiter_DB then
    CraterBaiter_DB = {
        logged = 0,
        logs = {}
    }
end

print("|cFF00FF00Crater Baiter|r v" .. "0.0.1" .. " loaded!")

-- colored class names
local CLASS_COLORS = {
    ["WARRIOR"] = "|cFFC79C6E",
    ["PALADIN"] = "|cFFF58CBA", 
    ["HUNTER"] = "|cFFABD473",
    ["ROGUE"] = "|cFFFFF569",
    ["PRIEST"] = "|cFFFFFFFF",
    ["DEATHKNIGHT"] = "|cFFC41F3B",
    ["SHAMAN"] = "|cFF0070DE",
    ["MAGE"] = "|cFF40C7EB",
    ["WARLOCK"] = "|cFF8787ED",
    ["MONK"] = "|cFF00FF96",
    ["DRUID"] = "|cFFFF7D0A",
    ["DEMONHUNTER"] = "|cFFA330C9",
    ["EVOKER"] = "|cFF33937F"
}

local function GetColoredClassName(classFile, className)
    local color = CLASS_COLORS[classFile] or "|cFFFFFFFF"
    return color .. (className or "Unknown") .. "|r"
end


local function GetUnitCoordinates(unit)
    local mapID = C_Map.GetBestMapForUnit(unit)

    if mapID and unit then
        local mapInfo = C_Map.GetMapInfo(mapID)
        local mapPos = C_Map.GetPlayerMapPosition(mapID, unit)
        
        -- TODO: implement x, y boundaries instead to zero in on crater
        if mapPos and mapInfo.name == "Hillsbrad Foothills" then
            local x, y = mapPos:GetXY()
            return x * 100, y * 100, mapInfo
        end
    else
        print("[DEBUG] unit: " .. unit .. " outside hillsbrad or unknown")
    end
    return nil, nil
end

-- Helpful portal CRUD functionality
local function logHelpfulPortal(name, realm, class, xPos, yPos, logTime)
    local helpedPlayer = {
        name = name,
        realm = realm,
        class = class,
        xPos = xPos,
        yPos = yPos,
        logTime = logTime
    }
    table.insert(CraterBaiter_DB.logs, helpedPlayer)
    CraterBaiter_DB.logged = #CraterBaiter_DB.logs

end

local function MenuHandler(owner, rootDescription, contextData)
    if not contextData or not contextData.name then
        return
    end
    rootDescription:CreateDivider()
    rootDescription:CreateButton("Log Helpful Portal", function()
        local unit = contextData.unit
        
        local targetName = contextData.name
        local targetClass = contextData.class
        local targetRealm = contextData.server or GetRealmName()
        local xPos, yPos = nil, nil
        local logTime = GetServerTime()
        -- TODO: possibly check if player is dead but not released
        local isUnreleasedCorpse = UnitIsDead(contextData.unit)
        if isUnreleasedCorpse then
            xPos, yPos = GetUnitCoordinates(contextData.unit)
        end

        local localizedClass, englishClass = UnitClass(contextData.unit)
        local classColored = GetColoredClassName(englishClass, localizedClass)

        -- Print result
        print("|--Name--|--Realm--|--Class--|--xPos--|--yPos--|--timestamp--|--debug--|")
        print(targetName .. " | " .. targetRealm .. " | " .. classColored .. " | " .. tostring(xPos) .. " | " ..  tostring(yPos) .. " | " .. tostring(logTime) .. " | " .. "true")
        
        logHelpfulPortal(targetName, targetRealm, targetClass, xPos, yPos, logTime)

    end)
end

-- Slash command setup
SLASH_CRATERBAITER1 = "/cb"
SlashCmdList["CRATERBAITER"] = function(msg)
    local cmd = string.lower(msg or "")
    
    if cmd == "say" then
        SendChatMessage("Hi!", "SAY")
    elseif cmd == "version" then
        print("|cFF00FF00Crater Baiter|r Version v0.0.1 by |cFF3477EBBarboosa|r")
    elseif cmd == "stats" then
        print("Helped |cFF3477EB".. tostring(#CraterBaiter_DB.logs) .. "|r Players find the Crater")
    else
        print("|cFF00FF00Crater Baiter|r Version v0.0.1 by |cFF3477EBBarboosa|r")
        print("Crater Baiter Commands:")
        print("-  /cb stats")
        print("-  /cb version")
    end
end

-- Hook into the context menu system
if Menu and Menu.ModifyMenu then
    local menuTags = {
        -- Players
        -- "MENU_UNIT_PLAYER",
        -- "MENU_UNIT_ENEMY_PLAYER", 
        "MENU_UNIT_PARTY",
        "MENU_UNIT_RAID_PLAYER",
        "MENU_UNIT_FRIEND",
        "MENU_UNIT_SELF",

        -- General
        -- "MENU_UNIT_TARGET",         -- Any target
        "MENU_UNIT_FOCUS",          -- Focus target
    }
    
    for _, tag in ipairs(menuTags) do
        Menu.ModifyMenu(tag, MenuHandler)
    end
end