from snowflake import connector

#snowflake
def sfconnect():
    cnx = connector.connect(
    account = {{sf_account}},
    user = {{db_user}},
    password = {{db_password}},
    warehouse = 'COMPUTE_WH',
    database = 'DEMO2',
    schema = 'PUBLIC',
    role = 'SYSADMIN'
    )
    return cnx
