let count=2;
function addPV(){
    let form=document.getElementById('create-dash');
    let input=document.createElement('input')
    input.type="text";
    input.name="pv-address";
    input.id=count
    input.placeholder="Process Variable " + count;
    form.appendChild(input);
    
    let delete_button=document.createElement('button');
    delete_button.formMethod="None";
    delete_button.innerHTML="Remove";
    delete_button.id=count+'button';
    delete_button.style.backgroundColor="Blue";
    delete_button.addEventListener('onclick', function(){
        deletePV(count)}
        );
    form.appendChild(delete_button);
    
    count++;
}


function deletePV(number){

    let pv=document.getElementById(number);
    console.log("del");
    pv.remove();
}