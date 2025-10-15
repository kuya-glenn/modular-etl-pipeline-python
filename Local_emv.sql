/*CREATE TABLE vehicle_data_staging(
    mfr_id  NUMBER(10) PRIMARY KEY,
    country VARCHAR2(255),
    mfr_commonname  VARCHAR2(255),
    mfr_name VARCHAR2(255),
    vehicletypes CLOB,
    date_fetched TIMESTAMP(6)
);*/


/*select * from vehicle_data_staging;*/
SELECT vs.MFR_ID, vs.COUNTRY, vs.MFR_COMMONNAME, vs.MFR_NAME,
        t.IsPrimary,
        t.Name
        FROM vehicle_data_staging vs,
        JSON_TABLE (vs.VEHICLETYPES,
            '$[*]' COLUMNS (
                            IsPrimary VARCHAR2(255) PATH '$.IsPrimary',
                            Name VARCHAR2(255) PATH '$.Name'
                            )) t;

        
select * from vehicle_data_staging;

/*
truncate table vehicle_data_staging;

rollback;
*/
