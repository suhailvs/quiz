$(document).ready(function(){
	var min_left=$("span.testtime").text();
	starttimer(min_left); 
	showquestion(1,"startexam");
	
	
	function showquestion(qnum,opt_sel){
	//opt ==0 for allbutton(ie back, nav etc) except next
		var examid=$("span.examid").text();
	 	var etype=$("ul.breadcrumb li#ExamName").text();
		var subj=$("ul li.active a.subject").text();
		alert($("li.active a.subject").attr("id"));
		
		var params ={ param1:examid, param2:etype,
			param3:subj, param4:qnum, param5:opt_sel };
		$.ajax({ url: "/show-question/",
			dataType: "json",
			data: params,			
			success: setResult });
	}
	//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			
	function makeImgFN(fn) {
		return("<img src='/static/img/quests/"+fn+".JPG' alt=''>");
	}
	
	$("li.sub").click(function() {
		if ($(this).hasClass("active")){
			alert("this is disabled");
		}
		else{
		 $("li.sub").removeClass("active");
		 $(this).addClass("active");
		 showquestion(1,"subject_changed");
		}			
	});
	
	function setBtnNavcolor(jdata){
		//must called when next, skip, subjects, back, reset buttons clicked
		$("button.btn-nav-quests").removeClass("disabled");
		//set current question button nav disabled
		var c_btn_nav="button#btn-nav"+jdata.qn;
		$(c_btn_nav).addClass("disabled");
		
		$("button.btn-nav-quests").removeClass("btn-success");
		//"s_opts": {"1": "1", "2": "4"} ie for q 2, optsel 4 etc	
		if (jdata.s_opts){
			//if selected_opt for current question set combo checked
			if (jdata.s_opts[jdata.qn]){
				var check_opt="input.ch"+jdata.s_opts[jdata.qn];
				$(check_opt).prop("checked", true);
			}			
			for (var i = 1; i < 5; i++){
				if (jdata.s_opts[i]){
					var c_opt="button#btn-nav"+i;
					$(c_opt).addClass("btn-success");				
				}
			}
		}
	}
	function setResult(jsonData) {			
		$(".questionnumber").text(jsonData.qn);
		
		if (jsonData.qn == 1)
			$("#btn-back").addClass("disabled");
		else if ($("#btn-back").hasClass("disabled"))
			$("#btn-back").removeClass("disabled");			
		setBtnNavcolor(jsonData);		
		$(".question-box").html(makeImgFN(jsonData.qst));
		for (var i = 1; i < 5; i++) {
			var c_opt="a#opt"+i;
			$(c_opt).html(makeImgFN(jsonData.opts[i-1]));
		}
	}	


	$("#btn-next").click(function() {
		//var optsel=getoptsel();
		var optsel=$("input:radio[name=Choices]:checked").val();
		if (!optsel){
			alert("You must select an Answer to Save");
		}
		else
		{
			//get questn qestionnumber	
			var questn = $(".questionnumber").text();
			showquestion(++questn,optsel);				
		}
	});
							
	$(".btn-nav-quests").click(function() {
		var questn=$(this).text();
		showquestion(questn,"nav_question");
	});					 
});
