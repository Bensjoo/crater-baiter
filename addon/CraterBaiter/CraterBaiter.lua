-- Load the addon DB
if not CraterBaiter_DB then
    CraterBaiter_DB = {
        logged = 0,
        logs = {}
    }
end
local debug = false
local appNameColored = "|cFF00FF00Crater Baiter|r"
local appVersionSemVer = "v1.0.0"
local function printVersion()
    print(appNameColored .. " ".. appVersionSemVer .. " by |cFF3477EBBarboosa|r" .. " | help: /cb")
end
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

local function getTimeStr(timeInt)
    local timeStr = timeInt and date("%m/%d %H:%M", timeInt) or "Unknown"
    return timeStr
end

local function GetUnitCoordinates(unit)
    local mapID = C_Map.GetBestMapForUnit(unit)

    if mapID and unit then
        local mapInfo = C_Map.GetMapInfo(mapID)
        local mapPos = C_Map.GetPlayerMapPosition(mapID, unit)
        
        -- TODO: implement x, y boundaries instead to zero in on crater
        if mapPos and (mapInfo.name == "Hillsbrad Foothills" or debug) then
            local x, y = mapPos:GetXY()
            return tonumber(string.format("%.2f",x * 100)), tonumber(string.format("%.2f",y * 100))
        end
    else
        if debug then
            print("[DEBUG] unit: " .. unit .. " outside hillsbrad or unknown")
        end
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
    if debug then
        print("======= |cFF3477EBDEBUG LOG DATA|r ======")
        print("name:    " .. tostring(name))
        print("realm:   " .. tostring(realm))
        print("class:   " .. tostring(class))
        if xPos then
            print("xPos:    " .. tostring(xPos))
            print("yPos:    " .. tostring(yPos))
        end
        print("logTime: " .. tostring(logTime))
        print("================================")
    
    if xPos then
        coords = string.format(" - at (%.2f, %.2f)", xPos, yPos)
    else
        coords = " - Failed to fetch x,y"
    end
    print(
        string.format(
            "[%s] %s Found Dalaran!%s | Total count: %d", 
            getTimeStr(logTime),
            GetColoredClassName(class, name .. "-" ..realm),
            coords,
            CraterBaiter_DB.logged
        )
    )
    end
end

local function removeLogEntry(logId)
    logId = tonumber(logId)
    
    if not logId or logId < 1 or logId > #CraterBaiter_DB.logs then
        print("|cFFFF0000Error:|r Invalid log ID. Use /cb list to see valid IDs.")
        return false
    end
    
    local removedEntry = CraterBaiter_DB.logs[logId]
    table.remove(CraterBaiter_DB.logs, logId)  -- Removes and shifts indices
    
    -- Update the counter to match actual array length
    CraterBaiter_DB.logged = #CraterBaiter_DB.logs
    
    print(string.format("|cFF00FF00Removed:|r #%d (%s) - %d remaining", 
          logId, GetColoredClassName(removedEntry.class, removedEntry.name .. "-" ..removedEntry.realm), CraterBaiter_DB.logged))
    
    return true
end

local function listLogs()
    if #CraterBaiter_DB.logs == 0 then
        print(appNameColored .. ": 0 players helped. Contribute by casting a portal to Dalaran Crater!")
        print("  - Right-click the friendly unit and press \"Log Helpful Portal\"")
        print("  - If the member is a corpse in the crater, the x,y coordinates will be logged")
        return
    end

    print("===== Crater log -- |cFF3477EB".. tostring(#CraterBaiter_DB.logs) .. "|r total =====")
    
    for i, log in ipairs(CraterBaiter_DB.logs) do
        local coords = ""
        if log.xPos and log.yPos then
            coords = string.format("- at (%.2f, %.2f)", log.xPos, log.yPos)
        end
        
        local timeStr = log.logTime and date("%m/%d %H:%M", log.logTime) or "Unknown"
        
        print(string.format("  [%d] %s %s %s", 
              i, GetColoredClassName(log.class, log.name .. "-" ..log.realm), timeStr, coords))
    end
end

local function flushLogs()
    print("Flushing logs...")
    CraterBaiter_DB = {
        logged = 0,
        logs = {}
    }
end

-- main target / raidframe rightclick functionality
local function MenuHandler(owner, rootDescription, contextData)
    if not contextData or not contextData.name then
        return
    end

    
    

    rootDescription:CreateDivider()
    rootDescription:CreateButton("Log Helpful Portal", function()
        -- self data
        local playerName = UnitName("player")
        local playerRealm = GetRealmName()
        
        -- target data
        local unit = contextData.unit
        local targetName = contextData.name
        local targetClass = contextData.class
        local targetRealm = contextData.server or playerRealm
        local localizedClass, englishClass = UnitClass(unit)
        -- self-check, enable self-log in debug mode
        if (playerName .. playerRealm == targetName .. targetRealm ) and (debug == false) then
            print("won't log self unless debug mode")
            return true
        end
            local logTime = GetServerTime()
        local xPos, yPos = nil, nil
        

        local isUnreleasedCorpse = UnitIsDead(unit)
        if isUnreleasedCorpse or debug then
            xPos, yPos = GetUnitCoordinates(unit)
        end
        

        logHelpfulPortal(targetName, targetRealm, englishClass, xPos, yPos, logTime)
    end)
end

-- script execution
printVersion()
-- Slash command setup
SLASH_CRATERBAITER1 = "/cb"
SlashCmdList["CRATERBAITER"] = function(msg)
    local cmd = string.lower(msg or "")
    if cmd == "debug" then
        print("CraterBaiter: Debug mode activated")
        debug = true
    elseif cmd == "list" then
        listLogs()
    elseif cmd == "version" then
        printVersion()
    elseif cmd == "stats" then
        print("Helped |cFF3477EB".. tostring(#CraterBaiter_DB.logs) .. "|r Players find the Crater")
    elseif cmd:match("^remove ") then
        local logId = cmd:match("^remove (%d+)")
        if logId then
            removeLogEntry(logId)
        else
            print("|cFFFF0000Usage:|r /cb remove <number>")
        end
    elseif cmd == "flush-logs" then
        if debug then
            flushLogs()
        else
            print("Can only flush logs in debug mode. run /cb debug")
        end
    else
        print("Crater Baiter Commands:")
        print("-  /cb stats")
        print("-  /cb version")
        print("-  /cb remove <id> - Remove log by ID")
        print("-  /cb list - show helped players")
    end
end

-- Hook into the context menu system
if Menu and Menu.ModifyMenu then
    local menuTags = {
        -- Players
        "MENU_UNIT_PLAYER",
        -- "MENU_UNIT_ENEMY_PLAYER", 
        "MENU_UNIT_PARTY",
        "MENU_UNIT_RAID_PLAYER",
        "MENU_UNIT_FRIEND",

        -- General
        -- "MENU_UNIT_TARGET",         -- Any target
        "MENU_UNIT_FOCUS",          -- Focus target
        "MENU_UNIT_SELF"
    }
    for _, tag in ipairs(menuTags) do
        Menu.ModifyMenu(tag, MenuHandler)
    end
end