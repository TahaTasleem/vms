import { Component, OnInit,Input } from '@angular/core';
import { SharedService } from '../shared.service';
import { FormBuilder, FormGroup ,Validators} from '@angular/forms';

@Component({
  selector: 'app-prereg',
  templateUrl: './prereg.component.html',
  styleUrls: ['./prereg.component.css']
})
export class PreregComponent implements OnInit {

  @Input() dep:any;
  a:number=0;
  Visitorlist:any=[];
  email_address:string='';
  visitorlistfromcnic:any=[];

  lastempId:any=0;
  lastdummyId:any=0;
  example:number=0;
  list:any=[];
  emp_list:any=[];
  public userForm:FormGroup;  
  id:number=0;
  visitor_name:string="";
  organization_name:string="";
  purpose:string="";
  cnic:string="";
  contact_no:string="";
  checkin_time:Date=new Date();
  // checkout_time:Date=new Date();
  position_name:string='';
  organization:string='';
  gender:string="";
  employee_number:number=0;
  employee_id:number=0;
  group_id:number=0;
  status2:string='';
  name :string='';
  // department_id:number=0;
  status:string='';

  keyword = 'name';
  

  constructor(private fb:FormBuilder,private service:SharedService) { 
    this.userForm=this.fb.group({
      id: ['', Validators.required],
      visitor_name:['',[
        Validators.required,
        Validators.minLength(3),
        Validators.maxLength(200)
      ]
        ],
      organization_name:['',[
        Validators.required,
        Validators.minLength(4),
        Validators.maxLength(15)
      ]
  ],
      purpose:['',[
        Validators.required,
        Validators.minLength(4),
        Validators.maxLength(150)
      ]
  ],
      cnic:['',[Validators.required,Validators.minLength(13), Validators.maxLength(13)]],
      contact_no:['', [Validators.required, Validators.maxLength(11), Validators.pattern("^((\\+92)?(0092)?(92)?(0)?)(3)([0-9]{9})$")]],
      // checkout_time:'',
      checkin_time:'',
      gender:"",
      employee_number:['', Validators.required],
      organization:'',
      position_name:'',
      status:'',
      email_address:'',
      group_id:0,
      status2:''
    });

  }

  ngOnInit(): void {
    this.EmpList();
    this.FetchEmployeeList();
    this.FetchGroupId();
  }

  // EmpListwithid(event:any){
  //   this.service.getEmplistidsearch(event.target.value).subscribe(data=>{
  //     this.emp_list=[data];
  //     console.log(this.emp_list)
  //   });
  // }
  EmpListwithname(event:any){
    this.service.getEmpListName(event.name).subscribe(data=>{
      this.emp_list=data;
      console.log(this.emp_list)
    });
  }
  get f() { return this.userForm.controls; }

  EmpList(){
    this.service.getEmpList().subscribe(data=>{
      this.list=data;
    });
  }
  FetchEmployeeList(){
    this.service.getSortAscVisitorList().subscribe(data=>{
      this.Visitorlist=data;
      this.lastempId = data[data.length-1];
      // this.id=this.lastempId.id;
    })
  }
  FetchGroupId(){
    this.service.getSortAscVisListByGroup().subscribe(data=>{
      // this.dummylist=data;
      this.lastdummyId = data[data.length-1];
      // this.id=this.lastempId.id;
    })
  }
  addForm(){
    this.id=this.userForm.get("id")?.value;
    // this.id = this.lastempId.id +1;
    this.visitor_name=this.userForm.get("visitor_name")?.value;
    this.organization_name= this.userForm.get("organization_name")?.value;
    this.purpose = this.userForm.get("purpose")?.value;
    this.cnic = this.userForm.get("cnic")?.value;
    this.contact_no =this.userForm.get("contact_no")?.value;
    // this.checkout_time = this.userForm.get("checkout_time")?.value;
    // this.checkout_time= new Date(0);
    this.checkin_time = this.userForm.get("checkin_time")?.value;
    this.gender = this.userForm.get("gender")?.value;
    this.employee_id=this.userForm.get("employee_number")?.value;
    this.status=this.userForm.get("status")?.value;
    this.status2=this.userForm.get("status2")?.value;
    this.group_id = this.userForm.get("group_id")?.value;
    var val={id:this.id,visitor_name:this.visitor_name,
      organization_name:this.organization_name,
      purpose:this.purpose,
      cnic:this.cnic,
      // checkout_time:this.checkout_time,
      contact_no:this.contact_no,gender:this.gender,
      checkin_time:this.checkin_time,
      employee_id:this.employee_id,
      status:this.status,
      status2:this.status2,
      group_id :this.group_id
    };
    // console.log(val);
      this.service.addVisitor(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  selectEvent(item:any) {
    // do something with selected item
  }

  onChangeSearch(search: string) {
    // fetch remote data from here
    // And reassign the 'data' which is binded to 'data' property.
  }

  onFocused(e:any) {
    // do something
  }

  selectEventCountry(item:any) {}

  onLocationSubmit() {}

  onCountryCleared(item:any, flag:boolean) {}

  customFilter = function (list:any[], query: string): any[] {
    console.log(list)
    return list.filter((x) =>
      x.name.toLowerCase().startsWith(query.toLowerCase())
    );
  };
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

    
  getVisitorfromcnic(event:any){
    this.service.getVisitFromcnic(event.target.value).subscribe(data=>{
      this.visitorlistfromcnic=data;
      console.log(data);
    })
  }
  getVisitorfromcontactno(event:any){
    this.service.getVisitFromcontactno(event.target.value).subscribe(data=>{
      this.visitorlistfromcnic=data;
      console.log(data);
    })
  }

  refresh(): void {
    window.location.reload();
  }
}
