from prompt_toolkit.completion import NestedCompleter,WordCompleter



COMMANDS_COMPLETER=NestedCompleter.from_nested_dict({
     "assoc":WordCompleter([".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".pages",".xls", ".xlsx", ".xlsm", ".ods", ".csv", ".tsv",".ppt", ".pptx", ".odp", ".key",".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".svg", ".avif", ".heic",".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".opus", ".mid",".mp4", ".mkv", ".avi", ".mov", ".webm", ".wmv", ".flv", ".3gp",".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz", ".zst",".exe", ".msi", ".app", ".dmg", ".deb", ".rpm", ".apk", ".ipa",".c", ".h", ".cpp", ".hpp", ".cs", ".java", ".py", ".go", ".rs", ".swift", ".kt",".html", ".htm", ".css", ".js", ".mjs", ".ts", ".jsx", ".tsx", ".wasm",".json", ".xml", ".yaml", ".yml", ".toml", ".sql", ".db", ".sqlite",".mdb", ".accdb", ".db", ".sqlite", ".sqlite3", ".dbf",".dwg", ".dxf", ".step", ".stp", ".iges", ".igs", ".stl", ".obj", ".3mf",".inp", ".dat", ".bdf", ".fem", ".msh", ".mesh", ".cas", ".cdb",".shp", ".shx", ".dbf", ".geojson", ".kml", ".kmz", ".gpx", ".las",".blend", ".fbx", ".obj", ".3ds", ".dae", ".glb", ".gltf",".fits", ".hdf", ".h5", ".nc", ".mat", ".nii", ".nii.gz",".ttf", ".otf", ".woff", ".woff2", ".eot",".epub", ".mobi", ".azw", ".azw3", ".fb2",".eml", ".msg", ".mbox", ".pst", ".ost",".ini", ".cfg", ".conf", ".env", ".properties",".pem", ".crt", ".cer", ".der", ".key", ".p12", ".pfx",".iso", ".img", ".dmg", ".vhd", ".vhdx", ".vmdk", ".qcow2",".dll", ".sys", ".drv", ".so", ".dylib", ".ko",".log", ".trace", ".etl",".bak", ".backup", ".old", ".tmp",".srt", ".vtt", ".ass", ".ssa", ".sub",".dcm", ".nii", ".nii.gz",".pak", ".wad", ".rom", ".sav", ".unity3d",".onnx", ".pt", ".pth", ".safetensors", ".ckpt", ".pb"]),
         
    "attrib":WordCompleter(["+r" ,"+a" ,"+s" ,"+h" ,"+i" ,"+o" ,"+x" ,"+v" ,"+p" ,
                   "+u" ,"+b" ,"-r" ,"-a" ,"-s" ,"-h" ,"-i" ,"-o" ,"-x" ,"-v" ,"-p" ,
                   "-u" ,"-b" ,"/S","/D","/L"]),
    "break":{"=":{"on":None,
                  "off":None}},
    "cd":WordCompleter(["\\d",]),
    'call':None,
    'chdir':WordCompleter(["\\d",]),
     'cls':None, 
     'cmd':WordCompleter(["/c", "/k", "/s", "/q", "/d", "/a", "/u","/t:", "/t:","/e:on", "/e:off",
            "/f:on", "/f:off","/v:on", "/v:off"]), 
     'color':None, 
     'comp':WordCompleter(["/d", "/a", "/l", "/n", "/c"]), 
     'copy':WordCompleter(["/d", "/v", "/n", "/y", "/-y", "/z", "/a", "/b"],), 
     'date':{"/t"}, 
     'dir':WordCompleter( ["/p", "/q", "/w", "/d","/a:","/o:","/t:","/s", "/b", "/l", 
          "/n", "/x", "/c", "/4"]), 
     'doskey':WordCompleter(["/reinstall","/listsize=","/macros","/macros:",
               "/history","/insert","/overstrike","/exename=","/macrofile="]), 
     'echo':WordCompleter(["on", "off"]), 
     'exit':{"/b"}, 
     'fc':WordCompleter(["/a", "/c", "/l", "/lb", "/n","/off[line]", "/t", "/u", "/w", "/", "/b"]), 
     'find':WordCompleter([["/v", "/c", "/n", "/i", "/off[line]"]]), 
     'findstr':WordCompleter(["/b", "/e", "/l", "/r", "/s", "/i", "/x","/v", "/n", "/m", "/o", "/p",
            "/f:", "/c:", "/g:","/d:", "/a:", "/off[line]"]), 
     'for':None, 
     'ftype':None, 
     'goto':None, 
     'help':None, 
     "hostname":None,
     'if':WordCompleter(["/i","not","ERRORLEVEL","exist","cmdextversion","defined","else "]), 
     'label':{"/mp"}, 
     'md':None, 
     'mkdir':None, 
     'mklink':WordCompleter(["/d", "/h", "/j"]), 
     'more':WordCompleter( ["/c", "/p", "/s", "/t"]), 
     'move':WordCompleter(["/y", "/-y"]), 
     'path':None, 
     'pause':None, 
     'popd':None, 
     'prompt':None, 
     'pushd':None, 
     'rd':WordCompleter(["/s", "/q"]), 
     'rem':None, 
     'ren':None, 
     'rename':None, 
     'replace':WordCompleter(["/a", "/p", "/r", "/w", "/s", "/u"]), 
     'rmdir':WordCompleter(["/s", "/q"]), 
     'set':WordCompleter(["/p", "/a"]), 
     'setlocal':WordCompleter(["enableextensions","disableextensions","enabledelayedexpansion",
            "disabledelayedexpansion"]), 
     'shift':{"/n"}, 
     'sort':WordCompleter(["/r", "/+", "/m","/l", "/rec","/t", "/o"]), 
     'start':WordCompleter(["/d","/i","/min", "/max","/separate", "/shared","/low", "/normal",
            "/high","/realtime", "/abovenormal", "/belownormal","/affinity","/wait","/b"]), 
     'subst':{"/d"}, 
     'tasklist':WordCompleter(["/s","/u","/p","/m","/svc","/v","/fo table","/fo list","/fo csv",
               "/nh","/fi"]), 
     'taskkill':WordCompleter(["/s","/u","/p","/fi","/pid","/im","/f","/t"]), 
     'time':None, 
     'title':None, 
     'tree':WordCompleter( ["/f", "/a"]), 
     'type':None, 
     'ver':None, 
     'verify':WordCompleter( ["on", "off"]), 
     'vol':None, 
     "whoami":None,
     'xcopy':WordCompleter(["/w", "/p", "/c", "/v", "/q", "/f", "/l", "/g","/d:", "/u", "/i", "/s",
          "/e","/t","/k", "/r", "/h", "/a", "/m", "/n", "/o", "/x","/exclude:","/y", "/-y", "/z",
           "/b", "/j"])

    
})





if __name__=="__main__":
     from prompt_toolkit.shortcuts import PromptSession,prompt
     
     session=PromptSession()


     text = session.prompt("> ", completer=COMMANDS_COMPLETER)
