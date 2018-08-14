<template>
	<div class="container">
	<div class="topbar">
		<h3>欢迎来到同步课堂</h3>
	</div>
	<div class="flex_container">
	<div class="sidebar">
		<button class="sidebar_btn">用户管理</button>
		<button @click="logout" class="sidebar_btn">退出登录</button>
	</div>
	
	<div class="main">
	    <table class="table">
	    	<thead class="thead-dark">
				 <tr>
			      <th scope="col">编号</th>
			      <th scope="col">姓名</th>
			      <th scope="col">邮箱</th>
			      <th scope="col">添加时间</th>
			      <th scope="col">操作</th>
			    </tr>
		  	</thead>
		  	<tbody>
		  		<tr class="table_items" v-for="(item,index) in items" >
					<!--<td ><input value="{{item.id}}"></td>-->
					<!--<td><input type="" name="" value="{{item.id}}" /></td>-->
					<template v-if="!item.type">
						<td >{{item.id}}</td>
						<td >{{item.username}}</td>
						<td >{{item.email}}</td>
						<td >{{item.datatime}}</td>
						<td><button @click='update(item,index,false)'  class="btn btn-primary">编辑</button>
							<button @click="deleteclick(item,index)" class="btn btn-danger">删除</button>
						</td>
					</template>
					<template v-else>
						<td >{{item.id}}</td>
						<td ><input v-model="item.username"></td>
						<td ><input v-model="item.email"></td>
						<td >{{item.datatime}}</td>
						<td><button @click='update(item,index,true)'  class="btn btn-primary">保存</button><button @click="cancelclick(item,index,true)" class="btn btn-danger">取消</button></td>
					</template>
				</tr>
				<tr>
					
				</tr>
		  	</tbody>
		    
	    </table>
    </div>
    </div>
    </div>
</template>

<script>
	console.log(localStorage.getItem("Tbkt-Token"))
	import qs from 'qs'
	export default {
	    name: 'index', 
	    data() { 
	 	    return {
	 		    items: []
	 	    }  
	    },
	    created() {
	     this.$http.post("/api/index/",{
	    		headers: {
      	  	  		'Content-Type': 'application/x-www-form-urlencoded', 
          	      	}
	    	})
	    	.then(response=>{
    	      	console.log(response.data)
    	      	// return false
			    this.msg =response.data
			    console.log(this.msg)
			    if(response.data.status == 'ok'){
			    	console.log(response.data.response)
			    	var userdata = response.data.response;
			    	userdata.map(data=>{
			    		data.type = false
			    	})
			    	this.items = userdata
		      		
		        }else{
		        	// alert("请先登录");
		        	this.$router.push('/');
		        }
		    })
      	    .catch(err=>{
             	console.log(err)
    	    })
        },
        methods: {
            deleteclick(item,index){
            	let deleteParam = { 
            			id: item.id
            	}
            	console.log(this.items)
            	this.$http.post("/api/delete/",qs.stringify(deleteParam), 
            		{ 
            			headers: { 
            				'Content-Type': 'application/x-www-form-urlencoded',
            			} 
            		}) 
            		.then(response=>{ 
            			console.log(response) 
            			if(response.data == 'ok'){
							//从项目或者数组中删除之前的项目， 然后返回被删除的项目
            				this.items.splice(index,1)
            			} 
            		}) 
            		.catch(
            			err=>{ console.log(err)
            			})
            		alert("删除")
            	
				},
			cancelclick(item,index){
				this.items[index].type = !this.items[index].type
				// userdata.map(data=>{
			    // 		data.type = false
			    // 	})
			},
            update(item,index,type){
            	this.items[index].type = !this.items[index].type
            	if(type){
            		console.log(item)
            		this.items[index] = item
            		let editParam = { 
            			id: item.id, 
            			username: item.username,
            			email: item.email
            		}
            		console.log(editParam) 
            		this.$http.post("/api/edit/",qs.stringify(editParam), 
            		{ 
            			headers: { 
            				'Content-Type': 'application/x-www-form-urlencoded',
            			} 
            		}) 
            		.then(response=>{ 
            			console.log(response) 
         			    this.msg =response.data 
            			if(response.data == 'ok'){
            				alert("保存成功！")
            			} 
            			else{
            				alert("保存失败！")
            			}
            		}) 
            		.catch(
            			err=>{ console.log(err)
            			})
            		
            	}
            },
            logout(){
            	localStorage.setItem("Tbkt-Token",'')
            	this.$router.push('/');
            }
        }
	}
	
</script>
<style>
	@import url("../../static/assets/bootstrap/css/bootstrap.css");
	.container{
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		width: 100%;
		height: 100%;
		/*background-image: url(../../static/assets/img/backgrounds/back.jpg);*/
	}
	.flex_container{
		width: 100%;
		height: 100%;
		/*background-color: lightgrey;*/
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
	.topbar{
		display: block;
		width: 100vw;
		height: 60px;
		background-color: lightgray;
		}
	.sidebar{
		background-color: darkgrey;
		height: 100vh;
		width: 150px;
		display: flex;
		flex-direction: column;
	}
	.sidebar_btn{
		font-weight: 600;
		background-color: darkgrey;
		line-height: 50px;
		color: #fff;
		border: none;
		display: block;	
		transition: all ease-out 0.2s;
	}
	.sidebar_btn:hover{
		background-color: #fff;
		color: black;
		transition: all ease-in 0.2s;
	}
	.main{
		padding-top: 5px;
		padding-left: 10px;
		display: block;
		width: calc(100vw - 150px);
		
	}
	.table_items{
		border-top: 1px solid lightgrey;
	}
	th{
        text-align:center;/** 设置水平方向居中 */
        vertical-align:middle/** 设置垂直方向居中 */
    }
</style>