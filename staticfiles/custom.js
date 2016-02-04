
$("#menu-toggle").click(function(e) {
	e.preventDefault();
	$("#wrapper").toggleClass("active");
});

$(document).ready(function(){


  function updateText(text) {
  $("#main").append(text);
  $(function () {$("html, body").animate({scrollTop: $('html, body').get(0).scrollHeight}, 2000);
  });
  }


 //Builds action buttons for content objects
  $(document).on("click", ".npc", function(){
	if ($(this).data("clicked")) return;
	$(this).data("clicked",1);
    var header = $(this).attr("header");
    var name = $(this).attr("name");
    var action = $(this).attr("action");
    var actCont = $(this).attr("actCont");
	$("#genactions").show();
    var actions = $(this).attr("action").split(" ");
	$("#sidebar-wrapper").append("<h3 class='actionheader'>What do you want to do with " + header + "?</h3>");
	for (var j=0; j<actions.length; j++) {
        $("#sidebar-wrapper").append("<div id=" + name + "><button type='button' class='btn btn-inverse action' actCont=" + actCont + " name=" + name + " action=" + actions[j] + ">" + actions[j] + "</button></div>");
      }
  });


  //Action Buttons
  $(document).on("click", ".action", function(){
	var name = $(this).attr("name");
	var action = $(this).attr("action");
    var actCont = $(this).attr("actCont");
    var genAct = $(this).attr("genAct");
    if ($(this).attr("genAct")) {
	  var gen_actions = $(this).attr("genAct").split(" ");
      for (var i=0; i<gen_actions.length; i++) {
        $("#sidebar-wrapper").append("<button type='button' class='btn btn-inverse action' name=" + name + " action=" + gen_actions[i] + ">" + gen_actions[i] + "</button>");
      }
    }
	if ($(this).attr("actCont")) {
	  var actions = $(this).attr("actCont").split(" ");
      for (var j=0; j<actions.length; j++) {
        $("#" + name).append("<button type='button' class='btn btn-inverse action' name=" + name + " action=" + actCont + ">" + actCont + "</button>");
      }
	}
	$(this).hide();
	$.post('/actions/', {action: action, name: name, actCont: actCont}, updateText);
  });

  //General forms
  $(document).on("click", ".form_but", function(){
	var name = $(this).attr("name");
	var action = $(this).attr("action");
	$(".form").hide();
	$(this).hide();
	var form_val = $('input[name=optionsRadios]:checked', '.form').val();
	$.post('/actions/', {name: name, action: action, form_val: form_val} , updateText);
  });

  $(document).on("click", ".hair_but", function(){
	var name = $(this).attr("name");
	var action = $(this).attr("action");
	$(".color_form").hide();
	$(".style_form").hide();
	$(this).hide();
	var hair_color = $('input[name=optionsRadios]:checked', '.color_form').val();
	var hair_style = $('input[name=optionsRadios1]:checked', '.style_form').val();
	$.post('/actions/', {name: name, action: action, hair_color: hair_color, hair_style: hair_style} , updateText);
  });

  //Name/Sex form
  $(document).on("click", ".sexform", function(){
	var name = $(this).attr("name");
	var action = $(this).attr("action");
	$(".sex").hide();
	$(this).hide();
	var sex = $('input[name=optionsRadios]:checked', '.sex').val();
	var charname = $("#nameform").val();
	$.post('/actions/', {name: name, action: action, charname: charname, sex: sex} , updateText);
  });

  //Wealth Form
  $(document).on("click", ".wealth", function(){
	var name = $(this).attr("name");
	var action = $(this).attr("action");
	$(".wealthform").hide();
	$(this).hide();
	var wealth = $('input[name=optionsRadios]:checked', '.wealthform').val();
	$.post('/actions/', {action: action, name: name, wealth: wealth}, updateText);
  });

});
