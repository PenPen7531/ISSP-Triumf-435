let date_box=document.getElementById("update-time");
let date=new Date();
date_box.innerHTML("Date"+date);
let meta_head = document.getElementById('refresh-rate');
console.log(meta_head)

function change_refresh_rate(){
    let meta_head = document.getElementById("refresh-rate");
    let input_data = document.getElementById("refresh_input").value;
    if (Number.isInteger(+input_data)){
        meta_head.content = input_data;
        console.log("Is num");
    }
    console.log(input_data);
    console.log(meta_head);
};