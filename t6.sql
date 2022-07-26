--------------------------------------------------------
--  File created - Tuesday-July-26-2022   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for View HPML_HR_ORGANIZATIONS
--------------------------------------------------------

  CREATE OR REPLACE FORCE EDITIONABLE VIEW "HPMLVMS"."HPML_HR_ORGANIZATIONS" ("ORGANIZATION_ID", "NAME") AS 
  select org.organization_id, org.name from apps.HR_ALL_ORGANIZATION_UNITS_TL org
;
