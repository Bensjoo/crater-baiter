print("|cFF00FF00Crater Baiter|r v" .. "0.0.1" .. " loaded!")
SLASH_CRATERBAITER1 = "/cb"

SlashCmdList["CRATERBAITER"] = function(msg)
    local cmd = string.lower(msg or "")
    
    if cmd == "say" then
        SendChatMessage("Hi!", "SAY")
    elseif cmd == "version" then
        print("|cFF00FF00Crater Baiter|r Version v0.0.1 by |cFF3477EBBarboosa|r")
    else
        print("Crater Baiter Commands:")
        print("-  /cb say - Say hi!")
        print("-  /cb version")
    end
end

-- Context menu functionality
local function MenuHandler(owner, rootDescription, contextData)
    if not contextData or not contextData.name then
        return
    end
    
    -- Don't show for yourself
    local playerName = UnitName("player")
    local playerRealm = GetRealmName()
    local fullPlayerName = playerName .. "-" .. playerRealm
    local targetName = contextData.name
    local targetRealm = contextData.server or GetRealmName()
    local fullTargetName = targetName .. "-" .. targetRealm
    
    if fullTargetName == fullPlayerName then
        return
    end
    
    -- Add our menu option
    rootDescription:CreateDivider()
    rootDescription:CreateButton("Print Name", function()
        -- Test with just your own coordinates first
        local playerMapID = C_Map.GetBestMapForUnit("player")
        local playerPos = C_Map.GetPlayerMapPosition(playerMapID, "player")
        
        print("=== DEBUG INFO ===")
        print("Your MapID:", playerMapID or "nil")
        print("Your Zone:", GetZoneText())
        print("Your SubZone:", GetSubZoneText())
        
        if playerPos then
            print(string.format("Your Position: %.1f, %.1f", playerPos.x * 100, playerPos.y * 100))
        else
            print("Your Position: nil")
        end
        
        -- Now try target
        local unit = contextData.unit or "target"
        print("Unit token:", unit)
        print("Unit exists:", UnitExists(unit))
        print("Unit name:", UnitName(unit) or "nil")
        print("Target name we want:", targetName)
        
        if UnitExists(unit) then
            -- local targetMapID = C_Map.GetBestMapForUnit(unit)
            targetMapID = playerMapID
            print("Target MapID:", targetMapID or "nil")
            
            if targetMapID then
                local targetPos = C_Map.GetPlayerMapPosition(playerMapID, unit)
                if targetPos then
                    print(string.format("Target Position: %.1f, %.1f", targetPos.x * 100, targetPos.y * 100))
                else
                    print("Target Position: nil")
                end
            end
        end
        print("==================")
    end)
end

-- Hook into the context menu system
if Menu and Menu.ModifyMenu then
    local menuTags = {
        "MENU_UNIT_PLAYER",
        "MENU_UNIT_ENEMY_PLAYER", 
        "MENU_UNIT_PARTY",
        "MENU_UNIT_RAID_PLAYER",
        "MENU_UNIT_FRIEND"
    }
    
    for _, tag in ipairs(menuTags) do
        Menu.ModifyMenu(tag, MenuHandler)
    end
end