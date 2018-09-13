# SQL Alchemy
import sqlalchemy
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.engine import reflection

#import egnine
from config import engine_url

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

# Pandas
import pandas as pd
import os
import numpy as np
import datetime 
# import numpy.float64

#flash and jasonify
from flask import Flask, jsonify, make_response, render_template, redirect, request


#################################################
# Database Setup
#################################################

engine = create_engine(engine_url)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__, static_url_path='/static')


#################################################
# Flask Routes
#################################################

# Static HTML Pages
#################################################
numberOfDays= 0
# @app.route("/")
# def welcome():
#     return render_template("index.html")

@app.route("/address")
def address_pg():
    return render_template('address.html')

@app.route("/email")
def email_pg():
    return render_template('email.html')

@app.route("/phone")
def phone_pg():
    return render_template("phone.html")

@app.route("/index")
def index_pg():
    return render_template("index.html")

@app.route("/team")
def team_pg():
    return render_template("team.html")

# Interactive Routes 
#################################################

@app.route("/address/<firm_id>")
def address(firm_id):
    # Query firm specific address fields
    sql_address = """ SELECT p.id as person_id, 
        pdata.street, 
        pdata.street_2, pdata.city,
        pdata.state,
        pdata.postal_code,
        pdata.country,
        reg.name as region,
        if(pdata.id = p.preferred_address_id, "preferred","") as preferred
        from `people` as p
        inner join person_addresses as pdata on p.id = pdata.person_id
        left join regions as reg on pdata.`region_id` = reg.id
        left join location_types as loc on pdata.location_type_id = loc.id
        where p.firm_id = %s
        order by person_id """
    address_df = pd.read_sql_query(sql_address, session, params=[firm_id])
    # address_csv = address_df.to_csv("address.csv", sep='\t', encoding='utf-8')
    # address_json = address_df.to_json()

    resp = make_response(address_df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=address.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route("/email/<firm_id>")
def email(firm_id):
    # SQL to split out email
    sql_email = """ SELECT p.id as person_id,
        pdata.`address` as email,
        loc.name as type,
        if(pdata.id = p.preferred_email_address_id, "preferred","") as preferred
        from `people` as p
        inner join person_email_addresses as pdata on p.id = pdata.person_id
        left join location_types as loc on pdata.location_type_id = loc.id
        where p.firm_id = %s
        order by person_id"""
    email_df = pd.read_sql_query(sql_email, session, params=[firm_id])
    # email_csv = email_df.to_csv("email.csv", sep='\t', encoding='utf-8')

    resp = make_response(email_df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=email.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route("/phone/<firm_id>")
def phone(firm_id):
    # SQL to split out email
    sql_phone = """SELECT p.id as person_id,
            pdata.digits as phone,
            pdata.extension as extension,
            loc.name as type,
            if(pdata.id = p.preferred_phone_number_id, "preferred","") as preferred
            from `people` as p
            inner join person_phone_numbers as pdata on p.id = pdata.person_id
            left join location_types as loc on pdata.location_type_id = loc.id
            where p.firm_id = %s
            order by person_id"""
    phone_df = pd.read_sql_query(sql_phone, session, params=[firm_id])
    # phone_df.to_csv("phone.csv", sep='\t', encoding='utf-8')

    resp = make_response(phone_df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=phone.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route("/activity", methods=["GET", "POST"])
def activity_pg():
    if request.method == 'POST':
        user1_id = request.form['UserID1']
        user2_id = request.form['UserID2']
        number_days = request.form['InputDays']
    else:
        user1_id = 2477
        user2_id = 2754
        number_days = 365
    global uid
    global no_of_days
    uid=[user1_id,user2_id]
    no_of_days=number_days
    return render_template('activity.html', User1ID=user1_id, User2ID=user2_id, NoOfDays=number_days)

@app.route("/test")
def test():
    # uid = [user1_id, user2_id]
    global uid
    global no_of_days
    # print(uid)
    both_user_data=[]
    for user in uid:
    # print(uid)
        sql_query = "SELECT * FROM events WHERE actor_id= %s"
        df = pd.read_sql_query(sql_query, session.bind, params=[user])
        i=0
        ifor_val=[]
        while i <len(df):
            ifor_val.append(df['updated_at'][i].date())
            i=i+1
        df['updated_at']=ifor_val   
        now = pd.datetime.now().date()
        t = str(no_of_days)+"days"
        new_df=df[df['updated_at'] > (now - pd.to_timedelta(t))]

        CandidacyCreation=int(new_df[new_df['type']=='CandidacyCreationEvent']['entity_type'].count())
        CandidacyStatusChange=int(new_df[new_df['type']=='CandidacyStatusChangeEvent']['entity_type'].count())
        CandidacyDeletion=int(new_df[new_df['type']=='CandidacyDeletionEvent']['entity_type'].count())
        NoteCreation=int(new_df[new_df['type']=='NoteCreationEvent']['entity_type'].count())
        NoteDeletion=int(new_df[new_df['type']=='NoteDeletionEvent']['entity_type'].count())
        NoteUpdate=int(new_df[new_df['type']=='NoteUpdateEvent']['entity_type'].count())
        StoplightChange=int(new_df[new_df['type']=='StoplightChangeEvent']['entity_type'].count())
        ProjectCreation=int(new_df[new_df['type']=='ProjectCreationEvent']['entity_type'].count())
        ProjectStatusChange=int(new_df[new_df['type']=='ProjectStatusChangeEvent']['entity_type'].count())
        x_axis=['CandidacyCreation','CandidacyStatusChange','CandidacyDeletion','NoteDeletion',\
        'NoteCreation', 'NoteUpdate','StoplightChange','ProjectCreation','ProjectStatusChange']
        y_axis=[CandidacyCreation,CandidacyStatusChange,CandidacyDeletion,NoteDeletion,NoteCreation,NoteUpdate,StoplightChange,ProjectCreation,ProjectStatusChange]
        data = {
        "x": x_axis,
        "y": y_axis,
        }
        both_user_data.append(data)
    # print(both_user_data)
    # print (t)
    return(jsonify(both_user_data))

@app.route('/names')
def names():
    # define SQL query
    sql_query = "SELECT DISTINCT actor_id FROM events"
    df23 = pd.read_sql_query(sql_query, session.bind)
    df23.fillna(0, inplace=True)
    return jsonify(list(df23['actor_id']))


@app.route("/waterfall", methods=["GET", "POST"])
def waterfall_pg():
    # get firm id from user, assign to firm id, input("enter firm Id")
    if request.method == 'POST':
        firm_id = request.form['firm_id']
        project_id = request.form['project_id']
    else:
        firm_id = 100
        project_id = '13847'

    # run statuses query with firm id as params
    # print("firm_id: " + str(firm_id))
    # print("project_id: " + str(project_id))
    sql_query = "SELECT rank, name FROM statuses where firm_id = %s"
    # turn status results into df and two lists;
    statuses = pd.read_sql_query(sql_query, session.bind, params=[firm_id])
    status_list = list(statuses['rank'])
    status_names = list(statuses['name'])
    
    # get candidate stats report 
    # to make dynamic run query on candidacy stats for * with firm id.
    data = pd.read_csv("SPMB_Active_Waterfall.csv")
    data = data.set_index('id')

    # get focused project data set.
    focus_project = data.filter(like=project_id, axis=0)
    # print(focus_project)

    # create empty lists to append function overview_chart data to;
    total = []
    in_list = []
    out = []
    current = []

    # function overview_chart gets waterfall data counts
    def overview_chart():

        for i in status_list:
        
            t=focus_project[focus_project['watermark_rank']>focus_project['status_rank']]
            IN_activity=t[t['watermark_rank']==i]
        
            t2=focus_project[focus_project['watermark_rank']==i]
            OUT_activity=t2[t2['status_rank']<=1000.0]
        
            t=focus_project[focus_project['status_rank']==i]
            CURRENT_activity=t[t['watermark_rank']==i]
        
            total.append(IN_activity['watermark_rank'].count()+OUT_activity['watermark_rank'].count()+CURRENT_activity['watermark_rank'].count())
            in_list.append(IN_activity['watermark_rank'].count())
            out.append(OUT_activity['watermark_rank'].count())
            current.append(CURRENT_activity['watermark_rank'].count())
            i=+i
        return()
    overview_chart()
    overview_df = pd.DataFrame(
        {'Rank' : status_list,
        'Status': status_names, 
        'Total': total, 
        'In': in_list, 
        'Out': out, 
        'Current': current},
        columns=['Rank','Status', 'Total', 'In', 'Out', 'Current'])
    overview_df = overview_df.sort_values(by=['Rank'])
    overview_df = overview_df.set_index('Status')
    overview_df = overview_df.drop(columns=['Rank', 'Total'])
    overview_df = overview_df[(overview_df.T != 0).any()]
    # clear all lists
    total.clear
    in_list.clear
    out.clear
    current.clear
    # print(project_id)
    # convert to json / html
    overview_json = overview_df.to_json()
    overview_html = overview_df.to_html()
    overview_csv = overview_df.to_csv('static/data.csv')
    
    # return overview_html #redirect("/events", code=302)
    return render_template('waterfall.html', df=overview_df, firm_id=firm_id, project_id=project_id, overview_html=overview_html)


sql_projects =""" SELECT 
                        proj.firm_id,
                        f.hostname,
                        proj.id as project_id, 
                        proj.name as project_title, 
                        proj.preferred_industry_id,
                        proj.client_company_id, 
                        i.name as industry_name,
                        i.parent_id,

                        pm.seniority_id,
                        s.name as seniority_name,
                        c.name as project_client,
                        proj.is_internal,
                        proj.is_confidential, 
                        proj.status,
                        proj.closing_reason_id as id,
                        cr.name as closing_reason,
                        DATEDIFF(proj.closed_at, proj.started_at) AS days_to_close,
                        date(proj.started_at) as start_day,
                        date(proj.closed_at) as closed_day,
                        if(SUBSTRING_INDEX(SUBSTR(email, INSTR(email, '@') + 1),'.',1)='clockworkrecruiting','migrated','internal') as project_source,
                            (select count(id)
                            from project_clients pc
                            where proj.id = pc.project_id) as client_count,
                            (select count(id)
                            from project_clients pc
                            where pc.viewed_at is not null
                            and proj.id = pc.project_id) as client_viewed,
                            (select count(cn.id)
                            from candidacy_notes cn
                            join vw_user_roles vu on cn.author_id = vu.user_id
                            join candidacies c on cn.candidacy_id = c.id
                            where vu.role_rank = 20 
                            and c.project_id = proj.id) as client_notes

                        FROM spmb_101.projects proj
                        LEFT JOIN spmb_101.firms f ON proj.firm_id = f.id
                        JOIN spmb_101.users u ON proj.owner_id = u.id
                        left join companies c on proj.client_company_id = c.id 
                        left join closing_reasons cr on proj.closing_reason_id = cr.id
                        left join industries i on proj.preferred_industry_id = i.id
                        left join project_metadata pm on proj.id = pm.project_id
                        left join seniorities s on pm.seniority_id = s.id

                        WHERE 
                        closed_at BETWEEN '2017-01-01' AND '2017-12-31' 
                        AND f.industry <> 5
                        AND proj.firm_id = %s
                        AND proj.status = 'closed' """

@app.route("/")
def project():
    firm_id = '100'
    global sql_projects
    # Query firm specific address fields

    projects_df = pd.read_sql_query(sql_projects, session.bind, params=[firm_id])
    # type(projects_df)
    projects_df.to_csv("static/project.csv")
    projectsDf = pd.DataFrame(projects_df)
    closingReasons = pd.DataFrame(pd.read_csv("static/closing_reasons.csv"))
    projects = pd.DataFrame(pd.merge(projectsDf, closingReasons, on="id"))
    projects.to_csv("static/projectFinal.csv")
    projects.to_json("static/projectFinal.csv")
    resp = make_response(projects.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=projectFinal.csv"
    resp.headers["Content-Type"] = "text/csv"

    def seniority():
        sql_projects 

        projects_df = pd.read_sql_query(sql_projects, session.bind)
        df1 = projects_df

        ##########################################
        #Setup dataframes with columns of interest
        #Clean out data that are NA and zero/negative
        ##########################################
        df2 = df1[["industry_name","seniority_name","start_day","seniority_id","days_to_close", "preferred_industry_id"]]
        df2 = df2.dropna(how="any")
        df2 = df2[df2["days_to_close"]>0]
        df2["start_day"] = pd.to_datetime(df2["start_day"])
        ########################################
        #Abbreviate columns
        ########################################
        df2.seniority_name.replace("Investor","Inv", regex=True, inplace=True)
        df2.seniority_name.replace("Director","Dir", regex=True, inplace=True)
        df2.seniority_name.replace("C-Level","C-L", regex=True, inplace=True)
        df2.seniority_name.replace("Board","BOD", regex=True, inplace=True)
        df2.seniority_name.replace("Other","Oth", regex=True, inplace=True)
        df2.seniority_name.replace("EVP/SVP","EVP", regex=True, inplace=True)

        ########################################
        #Determine the days from minimum day in the dataset for reference time plot
        ########################################
        df2 = df2.sort_values("start_day")
        df2["min_day"] = df2["start_day"]

        i = 0
        while i<len(df2):
            df2["min_day"][i] = min(df2["start_day"])
            i = i+1

        df2["reference_time"] = df2["start_day"] - df2["min_day"]
        # df2["reference_time"] = df2["reference_time"]/np.timedelta64(1,'D')

        df2 = df2.dropna(how="any")
        df2 = df2[df2["reference_time"]>0]
        #     ########################################
        #     #Generate output file for D3 graphing
        #     ########################################
        df2.to_csv("static/data_seniority.csv")
    return render_template('index.html')

@app.route("/tableData")
def tableData():
    firm_id = '100'
    # Query firm specific address fields
    global sql_projects

    projects_df = pd.read_sql_query(sql_projects, session.bind, params=[firm_id])

    projects_df.to_csv("static/project.csv")
    projectsDf = pd.DataFrame(projects_df)
    closingReasons = pd.DataFrame(pd.read_csv("static/closing_reasons.csv"))
    projects = pd.DataFrame(pd.merge(projectsDf, closingReasons, on="id"))

    i=0
    while( i<projects['industry_name'].size):
        if (projects['parent_id'][i] == 1):
            projects['industry_name'][i] = "Banking & Finance",
        elif (projects['parent_id'][i] == 20):
            projects['industry_name'][i] = "Consumer Internet"
        elif (projects['parent_id'][i] == 29):
            projects['industry_name'][i] = "Education"
        elif (projects['parent_id'][i] == 35):
            projects['industry_name'][i] = "Energy & Utilities"
        elif (projects['parent_id'][i] == 44):
            projects['industry_name'][i] = "Government & Non Profit"
        elif (projects['parent_id'][i] == 67):
            projects['industry_name'][i] = "Health Care"
        elif (projects['parent_id'][i] == 78):
            projects['industry_name'][i] = "Manufacturing"
        elif (projects['parent_id'][i] == 112):
            projects['industry_name'][i] = "Media"
        elif (projects['parent_id'][i] == 124):
            projects['industry_name'][i] = "Retail"
        elif (projects['parent_id'][i] == 139):
            projects['industry_name'][i] = "Services"
        elif (projects['parent_id'][i] == 176):
            projects['industry_name'][i] = "Tech Hardware"
        else:
            projects['industry_name'][i] = "Tech Software & Services"
        i=i+1

    daysToClose = projects['days_to_close'].to_json()
    seniorityName = projects['seniority_name'].to_json()
    industryName = projects['industry_name'].to_json()
    projectList = projects['project_id'].to_json()
    closingReason = projects['name'].to_json()

    dataTable = {}
    dataTable['daysToClose'] = daysToClose
    dataTable['seniorityName'] = seniorityName
    dataTable['industryName'] = industryName
    dataTable['projectList'] = projectList
    dataTable['closingReason'] = closingReason
    # print(dataTable)

    return jsonify(dataTable)



@app.route("/d3")
def calld3():
    # firm_id=firm_id, month=month, year=year
    return render_template("d3.html")

if __name__ == '__main__':
    app.run(debug=True)