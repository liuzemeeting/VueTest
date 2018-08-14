<template>
	<div class="top-content">

	<div class="inner-bg">
		<div class="container">
			<div class="row">
				<div class="col-sm-8 col-sm-offset-2 text">
					<h1><strong>Bootstrap</strong> Login Form</h1>
					<div class="description">
						<p>
							This is a free responsive login form made with Bootstrap. Download it on
							<a href="#"><strong>AZMIND</strong></a>, customize and use it as you like!
						</p>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col-sm-6 col-sm-offset-3 form-box">
					<div class="form-top">
						<div class="form-top-left">
							<h3>注 册 界 面</h3>
							<p>输 入 你 的 账 号 密 码 进 行 注 册:</p>
						</div>
						<div class="form-top-right">
							<i class="fa fa-key"></i>
						</div>
					</div>
					<div class="form-bottom">
						
						<div class="form-group">
								<label class="sr-only" for="form-username">账 号:</label>
								<!--<input type="text" placeholder="Email" :class="'log-input' + (account==''?' log-input-empty':'')" style="width: 500px;" v-model="account">-->
								<input type="text" name="form-username" placeholder="请输入你的账号!" class="form-username form-control" ref="account">
							</div>
							<div class="form-group">
								<label class="sr-only" for="form-password">密 码:</label>
								<!--<input type="password" placeholder="Password" :class="'log-input' + (passwords==''?' log-input-empty':'')" style="width: 500px;" v-model="passwords">-->
								<input type="password" name="form-password" placeholder="请输入你的密码!" class="form-password form-control" ref="passwords">
							</div>
							<button style="width: 500px;" @click="registerclick" class="btn">注 册</button>
						
						<center><a href="/">已有账号，快去登录</a></center>
					</div>

				</div>
			</div>
		</div>
	</div>

</div>
</template>

<script>
	import qs from 'qs'
	export default {
	    name: 'regist', 
	    data() { 
	 	    return {
	 		    account: '',
	  		    passwords: ''
	 	    }
	    },
	    methods:{
			registerclick(){
				if(this.$refs.account.value!='' && this.$refs.passwords.value!=''){
	  			    this.toLogin();
	  		    }
				else{
					alert("账号密码不能为空！")
				}
				
			},
			toLogin(){
				let loginParam = {
	  			    account: this.$refs.account.value,
	  			    passwords: this.$refs.passwords.value,
	  	        } 
	  	        console.log(loginParam)
	  	        this.$http.post("/api/register/",qs.stringify(loginParam),
     	    	   	{
        	    		headers: {
      	  	  		    'Content-Type': 'application/x-www-form-urlencoded', 
          	      	    }
    	      	    })
    	      	    .then(response=>{
    	      	    	console.log(response)
			      	    this.msg =response.data
			      	    console.log(this.msg)
			      	    if(response.data == 'ok'){
		      				this.$router.push('/');
		            	}
		      	    })
      	      	    .catch(err=>{
             	 		console.log(err)
    	            })

			}
		}
	}
</script>
 
<style>
	.top-content{
		margin-top: 0px;
		background-image: url(../../static/assets/img/backgrounds/1@2x.jpg);
	}
</style>