import { Component, OnInit } from '@angular/core';

import { SharedService } from 'src/app/shared.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ActivatedRoute ,Params} from '@angular/router';

@Component({
  selector: 'app-form2',
  templateUrl: './form2.component.html',
  styleUrls: ['./form2.component.css']
})
export class Form2Component implements OnInit {

  list:any=[];
  a:number=0;


  public userForm:FormGroup;  
  id:number=0;
  lastdummyId:any=0;
  visitor_name:string="";
  organization_name:string="";
  purpose:string="";
  cnic:string="";
  contact_no:string="";
  checkin_time:Date=new Date();
  // checkout_time:Date=new Date();
  gender:string="";
  employee_id:number=0;
  status:string='';
  group_id:number=0;
  status2:string='';
  id1:any='';

  constructor(private fb:FormBuilder,private service:SharedService,private route: ActivatedRoute) { 
    this.userForm=this.fb.group({
      id:'',
      visitor_name:"",
      organization_name:"",
      purpose:"",
      cnic:"",
      contact_no:"",
      // checkout_time:'',
      checkin_time:'',
      gender:"",
      employee_id:0,
      group_id:0,
      status:'',
      status2:'',
    });

  }

  ngOnInit(): void {
    this.route.params.subscribe((param : Params) => {
      this.id = param['id'];
  });
  this.EmpList(this.id);
  this.FetchGroupId();
  }

  EmpList(id:number){
    this.service.getEmpListId(id).subscribe(data=>{
      this.list=[data];
      console.log([data]);
    });
  }

  FetchGroupId(){
    this.service.getSortAscVisListByGroup().subscribe(data=>{
      // this.dummylist=data;
      this.lastdummyId = data[data.length-1];
      // this.id=this.lastempId.id;
    })
  }

  editForm(){
    this.id=this.userForm.get("id")?.value;
    this.visitor_name=this.userForm.get("visitor_name")?.value;
    this.organization_name= this.userForm.get("organization_name")?.value;
    this.purpose = this.userForm.get("purpose")?.value;
    this.cnic = this.userForm.get("cnic")?.value;
    this.contact_no =this.userForm.get("contact_no")?.value;
    this.checkin_time = this.userForm.get("checkin_time")?.value;
    this.gender = this.userForm.get("gender")?.value;
    this.employee_id=this.userForm.get("employee_id")?.value;
    this.status = this.userForm.get("status")?.value;
    this.status2 = this.userForm.get("status2")?.value;
    this.group_id = this.userForm.get("group_id")?.value;
    var val={id:this.id,visitor_name:this.visitor_name,
      organization_name:this.organization_name,
      purpose:this.purpose,
      cnic:this.cnic,
      // checkout_time:this.checkout_time,
      contact_no:this.contact_no,gender:this.gender,
      status:this.status,
      checkin_time:this.checkin_time,
      employee_id:this.employee_id,
      status2:this.status2,
      group_id:this.group_id
    };
      console.log(val);
      this.service.editVisitorfromId(this.id,val).subscribe(res=>{
      alert(res.toString());
    });
  }

  selectGroupId(event:any){
    if(this.lastdummyId.status2=="Group" && event.target.value=="Individual")
    {
      this.a=this.a+1;
      if(this.a==1){
      this.lastdummyId.group_id= this.lastdummyId.group_id + 1;console.log('ok1')}
    }
    if(this.lastdummyId.status2=="Group" && event.target.value=="Group")
    {
      this.a=this.a+1;
      if(this.a==1){
      this.lastdummyId.group_id = this.lastdummyId.group_id;console.log('ok2');}
    }
    if(this.lastdummyId.status2=="Individual" && event.target.value =="Group")
    {
      this.a=this.a+1;
      if(this.a==1){
      this.lastdummyId.group_id= this.lastdummyId.group_id + 1;
      console.log('ok3')}
    }
    if(this.lastdummyId.status2=="Individual" && event.target.value =="Individual"){
      this.a=this.a+1;
      if(this.a==1){
      this.lastdummyId.group_id= this.lastdummyId.group_id + 1;
      console.log('ok4')
    }
    }
    if(event.target.value=="New Group"){
      this.a=this.a+1;
      if(this.a==1){
      this.lastdummyId.group_id= this.lastdummyId.group_id + 1;}
    }
  }

  refresh(): void {
    window.location.reload();
  }

}
