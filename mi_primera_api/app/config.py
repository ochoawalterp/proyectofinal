class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.lwybdtzwdaouuxppydfm:1234@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
                            
    #'postgresql://postgres.rpcstciaxktztdvrdbqu:Walter#$123*#$@aws-0-us-east-1.pooler.supabase.com:6543/postgres'
    #'postgresql://postgres.tdombryjwohhttoypepj:Walter#$123*#$@aws-0-us-east-1.pooler.supabase.com:6543/postgres'                         
    JWT_ALGORITHM = 'HS256'
    SECRET_KEY = '14c6a8e28b197b71578132776d679a17ef402e8c'
    PROPAGATE_EXCEPTIONS = True    


