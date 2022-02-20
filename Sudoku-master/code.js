document.addEventListener('DOMContentLoaded',()=>{
 let boxes=Array.from(document.querySelectorAll('.gameArea div'))
 let numbers=Array.from(document.querySelectorAll('.numbers div'))
 let defaultValues=[]
 let Vertical=false,Horizontal=false,Diagonal=false,Box1=false
 let safeMove=true
 let gameOver=false
 
 
 //console.log(boxes)
 let currentBox=0
 let current
 clickedButton=0
 clickedNumber=0
 
 //assign class for the boxes
 function assingClass(){
  
   for(let i=0;i<boxes.length;i++)
   {
	 boxes[i].classList.add('box'+i)
	 if(i<numbers.length)numbers[i].classList.add('number'+i)
	 defaultValues[i]=false
   }
  }
  assingClass()
  //console.log(boxes)
  let buttons=[]
  
  //assign value for the for the div
  function assignValue(){
    for(let i=0;i<boxes.length;i++)
	{
	  document.querySelector(".box"+i).innerHTML += "<button></button>";
	  if(i<numbers.length)document.querySelector(".number"+i).innerHTML += "<button></button>";
	  buttons[i]=0
	  
	}
	
  }
  assignValue()
  var value=[3,4,1,9,6,2,3,7,8,2,7,4,9,1,3,6,7,5,8,1,1,2,9,6,4,8,2,5,3,3,6,7,9,1,7,6]
  var position=[0,2,4,9,14,15,16,17,18,19,21,24,25,26,28,30,31,39,40,42,47,48,50,51,52,53,58,59,60,65,67,68,69,72,78,80]
  //[8,5,8,3,5,4,1,7,8,6,5,9,3,2,3,8,1,7,3,4,2,1,1,8,6,9,7,2,5,4,5]
  //[0,2,12,14,15,16,19,24,26,27,31,33,34,37,39,40,41,43,46,47,49,53,54,56,62,65,66,67,69,78,80]
  
  
  //assign class for the buttons
  let boxValues=Array.from(document.querySelectorAll('.gameArea button'))
  let numberValues=Array.from(document.querySelectorAll('.numbers button'))
  
  function assignButtonClass(){
  
   for(let i=0;i<boxValues.length;i++)
   {
	 boxValues[i].classList.add('button'+i)
	 if(i<numbers.length)numberValues[i].classList.add('numbeB'+i)
	 
   }
  }
  assignButtonClass()
 
  
   function assignInitialValues()
   {
     for(let i=0;i<value.length;i++)
	 {
	  var a=position[i]
	  boxValues[a]=value[i]
	  buttons[a]=value[i]
	  defaultValues[a]=true
	 }
   }
   assignInitialValues()
   //console.log(boxValues)
   //console.log(buttons)
   //console.log(value.length)
   //console.log(position.length)
   
   //to assign boxvalues to the block
   
   
   //assign value for the for the div
  function assignBoxValue(){
		for(let i=0;i<boxValues.length;i++)
		{
		  let a=i+1
		  if(buttons[i]!=0)
		  {
		    if(buttons[i]==-1)document.querySelector(".button"+i.toString()).innerHTML="";
			else
		    document.querySelector(".button"+i.toString()).innerHTML=" "+buttons[i]+" ";
		  }
		  if(i<numbers.length)
		  {
		   if(i<numbers.length-1)document.querySelector(".numbeB"+i.toString()).innerHTML=" "+a+" ";
		   else document.querySelector(".numbeB"+i.toString()).innerHTML=" "+"del"+" ";
		  }
		}
	
	}
	
	assignBoxValue()
	//add action listener for each button
	var x=""
	var colorUpdate=""
	let colorAssigner
	let previousColorAssinger
	function assignbuttonclickListener(e)
	{
	 if(!gameOver)
	 {
				x=e.target.className+""
			 
			 if(x.charAt(0)=='n')
			 {
				
				console.log("clicked number is "+x.substring(6,8))
				clickedNumber=parseInt(x.substring(6,8))
				
			 }
			 else clickedNumber=-1
			 if(x.charAt(0)=='b')
			 {
			   colorUpdate=x+""
			  //console.log("clicked box is "+x.substring(6,8))
			   colorAssigner=document.getElementsByClassName("button"+clickedButton+"")
			   colorAssigner[0].style.border = "0px solid #0000FF";
			   clickedButton=parseInt(x.substring(6,8))
			   
			 }
			 console.log(x)
			 
			 if(clickedNumber!=-1&&clickedNumber!=9 && defaultValues[clickedButton]!=true)
			 {
			 buttons[clickedButton]=clickedNumber+1
			 colorAssigner=document.getElementsByClassName("button"+clickedButton+"")
			 colorAssigner[0].style.color = "blue";
			 colorAssigner[0].style.border = "1px solid #0000FF";	 
			 }
			 else if(clickedNumber==9)
			 {
			   //console.log("del is clicked")
			   //console.log(clickedButton,buttons[clickedButton])
			   //console.log(colorUpdate)
			   //console.log(value.length)
			  
			   buttons[clickedButton]=-1
			   assignBoxValue()
			 }
			 assignBoxValue()
			 //console.log(buttons,defaultValues)
			 checkValue()
			 if(!safeMove && defaultValues[clickedButton]!=true){
			 colorAssigner[0].style.color = "red"
			 safeMove=true
			 Vertical=false
			 Horizontal=false
			 Diagonal=false
			 Box1=false}
			 assignBoxValue()
			 checkGameOver()
			 if(gameOver)
			 {
			  alert("You won")
			   document.querySelector(".you-won").innerHTML="You Won!!!";
			  
			 }
			 
	 }
	 }
	document.addEventListener('click',assignbuttonclickListener)
	
	
	//to check if the user had a correct input
	
	function checkValue()
	{
	  checkDown()
	  checkHorizontal()
	  //checkDiagonal()
	  checkBox()
	  if(Vertical==true || Horizontal==true ||Diagonal==true||Box1==true)
	    safeMove=false
	  else safeMove=true
	}
	
	function checkDown()
	{
	  let coloumn=clickedButton%9
	  //console.log(coloumn)
	  let count=0
	  for (let i=0;i<9;i++)
	  {
	    if(buttons[i*9+coloumn]==buttons[clickedButton]&& defaultValues[clickedButton]!=true  &&  buttons[i*9+coloumn]!=0)count++
	    
	  }
	  if(count>1)Vertical=true
	}
	
	function checkHorizontal()
	{
	  let coloumn=parseInt((clickedButton/9)+"")
	  //console.log(coloumn)
	  let count=0
	  for (let i=0;i<9;i++)
	  {
	    if(buttons[coloumn*9+i]==buttons[clickedButton]&& defaultValues[clickedButton]!=true  &&  buttons[coloumn*9+i]!=0)count++
	    
	  }
	  if(count>1)Horizontal=true
	  //console.log(count)
	}
	
	function checkDiagonal()
	{
	  if(clickedButton%8==0)
	  {
	    let coloumn=parseInt((clickedButton/8)+"")
		  console.log(coloumn)
		  let count=0
		  for (let i=0;i<9;i++)
		  {
			if(buttons[8*(i+1)]==buttons[clickedButton]&& defaultValues[clickedButton]!=true  &&  buttons[8*(i+1)]!=0)count++
			
		  }
		  if(count>1)Diagonal=true
		  console.log(count)
	  }
	  else if(clickedButton%10==0)
	  {  
	      let coloumn=parseInt((clickedButton/10)+"")
		  console.log(coloumn)
		  let count=0
		  for (let i=0;i<9;i++)
		  {
			if(buttons[10*i]==buttons[clickedButton]&& defaultValues[clickedButton]!=true  &&  buttons[10*i]!=0)count++
			
		  }
		  if(count>1)Diagonal=true
		  console.log(count)
	  }
	  
	}
	
	function checkBox()
	{
	  box1=[0,1,2,9,10,11,18,19,20]
	  box2=[3,4,5,12,13,14,21,22,23]
	  box3=[7,8,9,15,16,17,24,25,26]
	  box4=[27,28,29,36,37,38,45,46,47]
	  box5=[30,31,32,39,40,41,48,49,50]
	  box6=[33,34,35,42,43,44,51,52,53]
	  box7=[54, 55, 56,63, 64, 65,72, 73, 74]
	  box8=[57, 58, 59,66, 67, 68,75, 76, 77]
	  box9=[60, 61, 62,69, 70, 71,78, 79, 80 ]
	  box=[box1,box2,box3,box4,box5,box6,box7,box8,box9]
	  
	  coloumn=parseInt((clickedButton/26)+"")
	  //console.log("row is "+coloumn)
	  if(clickedButton%9==0 ||clickedButton%9==1||clickedButton%9==2)coloumn=coloumn*0+coloumn
	  else if(clickedButton%9==3 ||clickedButton%9==4||clickedButton%9==5)coloumn*1+coloumn+1
	  else if(clickedButton%9==6 ||clickedButton%9==7||clickedButton%9==8)coloumn*2+coloumn+2
      //console.log("the button is on box "+coloumn)
	  //console.log(clickedButton)
	  
	  let count=0 
	  for(let i=0;i<9;i++)
	  {
	    if(box[i].includes(clickedButton))
		{
		  for(let j=0;j<9;j++)
		  {
		    if(buttons[clickedButton]==buttons[box[i][j]]&& defaultValues[clickedButton]!=true  &&  buttons[box[i][j]]!=0)count++
		  }
		  //console.log(box[i],clickedButton)
		  break
		}
	  }
	  if(count>1)Box1=true
     	  
	}
	
	function checkGameOver()
	{
	  gameOver=true
	  for(let i=0;i<81;i++)
	  {
	    if(buttons[i]==0||buttons[i]==-1)
		{
		 gameOver=false;
		 break;
		}
	  }
	}
	
	
	
	
	
	
	
	
  
  
  
  
  
  
 
  

})