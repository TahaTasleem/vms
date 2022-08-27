import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable  } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) { }

  getDeptList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/department')
  }

  addDept(val:any){
    return this.http.post(this.APIUrl + '/department/',val)
  }

  updateDept(val:any){
    return this.http.put(this.APIUrl + '/department/',val)
  }
  deleteDept(val:any){
    return this.http.delete(this.APIUrl + '/department/'+val)
  }

  getVisitorList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/newappointment')
  }
  CountVisitorStatus(name:string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/visitor/filter/count/'+name)
  }
  getVisitorFromStatus(name:string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/visitor/filter/'+name)
  }
  addVisitor(val:any){
    return this.http.post(this.APIUrl + '/newappointment/',val)
  }

  updateVisitor(val:any){
    return this.http.put(this.APIUrl + '/newappointment/',val)
  }
  deleteVisitor(val:any){
    return this.http.delete(this.APIUrl + '/newappointment/'+val)
  }
  getSortDescVisitorList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/visitor/desc')
  }
  getSortAscVisitorList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/visitor/asc')
  }
  getSortAscVisListByGroup():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/visitorbygroup/asc')
  }
  getVisitorFromId(id:number): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl+'/visitor/'+id);
  }
  getVisitorFromName(name:string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/visitors/'+name);
  }
  editVisitorfromId(id:any,val:any){
    return this.http.put(this.APIUrl+'/newappointmentedit/'+id,val);
  }
  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee')
  }
  getEmplistidsearch(id:number):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/'+id);
  }
  getEmpListId(id:number):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/newappointments/'+id);
  }
  getEmpListName(id:string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/'+id);
  }
  getEmpNamefromVisitor(id:string):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employeefromvisitor/'+id);
  }
  abc(val:any,id:number){
    return this.http.put(this.APIUrl + '/abc/'+id,val);
  }
  addEmp(val:any){
    return this.http.post(this.APIUrl + '/employee/',val)
  }

  updateEmp(val:any){
    return this.http.put(this.APIUrl + '/employee/',val)
  }
  deleteEmp(val:any){
    return this.http.delete(this.APIUrl + '/employee/'+val)
  }
  getVisitFromcontact(val:string){
    return this.http.get(this.APIUrl+'/visitorsearch/'+val)
  }
  
  getVisitFromcnic(val:string){
    return this.http.get(this.APIUrl+'/visitorsearchs/'+val)
  }
  getVisitFromcontactno(contact:string){
    return this.http.get(this.APIUrl + '/visitorsearchcontact/' +contact)
  }
  getEmpfromview(){
    return this.http.get(this.APIUrl + '/emp_view/')
  }

  sortvisitorstatus(status:string){
    return this.http.get(this.APIUrl+'/sortstatus/'+status);

  }
}
