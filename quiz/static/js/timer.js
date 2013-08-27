var down;	
var cmin,csec;

function starttimer(counter){
	 
	time = counter+":00";
	tsec= 0;
	Down();
	loaded = 1;
	}
function Minutes(data) {
	for(var i=0;i<data.length;i++) if(data.substring(i,i+1)==":") break;
	return(data.substring(0,i)); 
}

function Display(min,sec) {
	var disp;
	if(min<=9) disp=" 0";
	else disp=" ";	
	disp+=min+":";
	if(sec<=9) disp+="0"+sec;
	else disp+=sec;			
	return(disp); 
}

function Down() {
	cmin=1*Minutes(time);
	csec=tsec;
	DownRepeat(); 
}

function DownRepeat() {	
	csec--;
	if(csec==-1) {
		csec=59;
		cmin--;
	}
	$(".testtime").html(Display(cmin,csec));
	if(((cmin==0) && (csec==0)) || ((cmin<0)&&(csec<=59))) {
		alert("Time up!!!");	
		window.open('FeedBack.html', "_parent");
	}
	else  {
		down=setTimeout("DownRepeat()",1000); 
	}
}	
loaded=0;
