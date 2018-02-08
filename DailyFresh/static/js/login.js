        //
        // function check_pwd() {
      	// 	var txt_value = $("#LoginInputPassword").val(); // 得到当前文本框的值
        //     var txt_name = $("#LoginInputUser").val();
        //     var result;
      	// 	if (txt_value == "") {
        //     	alert("密码不能为空！");
			// 	result= false;
        //     }
     	// 	else {
      	// 	    $.ajax({
			// 	type:"POST",
			// 	async:false,
			// 	url:"/user/checkPwd/",
			// 	data:{name:txt_name, pwd:txt_value, csrfmiddlewaretoken: '{{ csrf_token  }}'},
			// 	dataType:"json",
			// 	success:function (data) {
			// 		alert(data.msg);
			// 		if(data.msg == "密码错误！"){
			// 			result =  false;
			// 		}
			// 		if(data.msg == "登录成功！"){
			// 			result =  true;
			// 		}
        //
        //     	}
			// })
			// }
			// return result;
        // }

	$(function () {



        $("#LoginInputUser").focus(function () { // 地址框获得鼠标焦点
      	    var txt_value = $(this).val(); // 得到当前文本框的值
     	    if (txt_value == "请输入用户名") {
     	    $(this).val(""); // 如果符合条件，则清空文本框内容
      		}
      		else{
     	    	$(this).val(""); // 如果符合条件，则清空文本框内容
			}

  		});

        $("#LoginInputUser").blur(function () { // 地址框失去鼠标焦点
      		var txt_value = $(this).val(); // 得到当前文本框的值
      		if (txt_value == "") {
         	$(this).val("请输入用户名"); // 如果符合条件，则设置内容
     		}
     		// else {
      		//     $.ajax({
			// 	type:"POST",
			// 	url:"/user/checkUname/",
			// 	data:{name:txt_value, csrfmiddlewaretoken: '{{ csrf_token  }}'},
			// 	dataType:"json",
			// 	success:function (data) {
			// 		if(data.msg=="用户名已存在！"){
            //
			// 		}
			// 		else{
			// 			alert("用户名不存在！");
			// 		}
            //
            	// }
			// })
			//}
 		})



        // $("#log_form").submit(function () {
        //
        //     if( ("#LoginInputPassword").val()!=""&& $("#LoginInputUser").val()!="请输入用户名"){
        //
        //         return true;
        //     }
        //     else {
        //
        //         return false;
        //     }
        // })
    })

