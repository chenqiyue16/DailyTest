

	$(function () {
		$("#inputUser").focus(function () { // 地址框获得鼠标焦点
      	    var txt_value = $(this).val(); // 得到当前文本框的值
     	    if (txt_value == "请输入用户名") {
     	    	$(this).val(""); // 如果符合条件，则清空文本框内容
      		}
  		});
 		 $("#inputUser").blur(function () { // 地址框失去鼠标焦点
      		var txt_value = $(this).val(); // 得到当前文本框的值
      		if (txt_value == "") {
         		$(this).val("请输入用户名"); // 如果符合条件，则设置内容
     		}
     		else {
      		    $.ajax({
				type:"POST",
				url:"/user/checkUname/",
				data:{name:txt_value, csrfmiddlewaretoken: '{{ csrf_token  }}'},
				dataType:"json",
				success:function (data) {

					if(data.msg == "用户名已存在！"){
						alert("用户名已存在！");
						$("#inputUser").val("请输入用户名");
					}
					else{

                    }
            	}
			})
			}
 		})

		$("#inputEmail").focus(function () { // 地址框获得鼠标焦点
      	    var txt_value = $(this).val(); // 得到当前文本框的值
     	    if (txt_value == "请输入邮箱") {
     	    $(this).val(""); // 如果符合条件，则清空文本框内容
      		}
  		});
 		 $("#inputEmail").blur(function () { // 地址框失去鼠标焦点
      		var txt_value = $(this).val(); // 得到当前文本框的值
      		if (txt_value == "") {
         	$(this).val("请输入邮箱"); // 如果符合条件，则设置内容
     		}
 		})


		$("#inputPassword2").blur(function () { // 地址框获得鼠标焦点
      	    var txt_value2 = $(this).val(); // 得到当前文本框的值
			var txt_value = $('#inputPassword').val()
     	    if (txt_value2 == txt_value || txt_value == "" || txt_value2 == "") {
     	     // 如果符合条件，则清空文本框内容
      		}
      		else{
			    alert("两次输入密码不一致！")
				$(this).val("");
			    $('#inputPassword').val("")
			}
  		});

 		$("#reg_form").submit(function () {
            if($("#inputPassword").val()!=""&& $("#inputUser").val()!="请输入用户名" && $("#inputEmail").val()!="请输入邮箱"){
                alert("注册成功！")
                return true;
            }
            else {
                alert("提交不能为空！")
                return false
            }
        })
    })

