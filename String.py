import pyrogram 
 
app = pyrogram.Client( 
    "session_name", 
    20037631, 
    "ee6caffb104ca333abff9c1d8b90b229", 
    in_memory=True 
) 
 
app.start() 
 
string_session = app.export_session_string() 
 
app.send_message("me", f"{string_session}") 
 
print("\n\nCHECK SAVED MESSAGES")
