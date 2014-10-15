DB_METHODS = """
    db.addUser(userDocument)
    db.adminCommand(nameOrDocument) - switches to 'admin' db, and runs command [ just calls db.runCommand(...) ]
    db.auth(username, password)
    db.cloneDatabase(fromhost)
    db.commandHelp(name) returns the help for the command
    db.copyDatabase(fromdb, todb, fromhost)
    db.createCollection(name, { size : ..., capped : ..., max : ... } )
    db.currentOp() displays currently executing operations in the db
    db.dropDatabase()
    db.eval(func, args) run code server-side
    db.fsyncLock() flush data to disk and lock server for backups
    db.fsyncUnlock() unlocks server following a db.fsyncLock()
    db.getCollection(cname) same as db['cname'] or db.cname
    db.getCollectionNames()
    db.getLastError() - just returns the err msg string
    db.getLastErrorObj() - return full status object
    db.getMongo() get the server connection object
    db.getMongo().setSlaveOk() allow queries on a replication slave server
    db.getName()
    db.getPrevError()
    db.getProfilingLevel() - deprecated
    db.getProfilingStatus() - returns if profiling is on and slow threshold
    db.getReplicationInfo()
    db.getSiblingDB(name) get the db at the same server as this one
    db.hostInfo() get details about the server's host
    db.isMaster() check replica primary status
    db.killOp(opid) kills the current operation in the db
    db.listCommands() lists all the db commands
    db.loadServerScripts() loads all the scripts in db.system.js
    db.logout()
    db.printCollectionStats()
    db.printReplicationInfo()
    db.printShardingStatus()
    db.printSlaveReplicationInfo()
    db.removeUser(username)
    db.repairDatabase()
    db.resetError()
    db.runCommand(cmdObj) run a database command.  if cmdObj is a string, turns it into { cmdObj : 1 }
    db.serverStatus()
    db.setProfilingLevel(level,<slowms>) 0=off 1=slow 2=all
    db.setVerboseShell(flag) display extra information in shell output
    db.shutdownServer()
    db.stats()
    db.version() current version of the server
"""

COLLECTION_METHODS = """
"""
