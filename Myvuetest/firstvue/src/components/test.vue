<template>
  <div>
    <p>{{ value }}<p>
    <p v-text="value"></p>
    <p v-html="value"></p>
    <p v-if="Math.random() > 0.5">Sorry</p>
    <p v-else>Not sorry</p>
    <div>
      <span v-for="n in 10">{{ n }} </span>
    </div>
    <div>
      <input type="file" name="file" class="upload__input" @change="uploadChange" accept="image/png,image/gif"> 
    </div>
    <!-- <p>Computed reversed message: "{{ reversedMessage }}"</p> -->
  </div>
</template>

<script>
export default {
  name: 'test',
  data(){
      return {
          'value': '<h3>我是h3标签</h3>'
      }
  },
  // methods:{
  //   uploadChange(event){  
  //     if(event.target.files.length>0){  
  //         this.files = event.target.files[0];  //提交的图片  
  //         this.$conf.getBase64(event.target,(url)=>{  
  //             this.imgDataUrl = 'data:image/png;base64,'+url;   //显示的图片  
  //         });   
  //     }  
            
  //   },
  // }
  methods: {
      //设置
      limitClick(state) {
        this.imgList = [];
        if (state)
          this.limit = 2;
        else
          this.limit = undefined;
      },
      fileClick() {
        document.getElementById('upload_file').click()
      },
      fileChange(el) {
        if (!el.target.files[0].size) return;
        this.fileList(el.target);
        el.target.value = ''
      },
      fileList(fileList) {
        let files = fileList.files;
        for (let i = 0; i < files.length; i++) {
          //判断是否为文件夹
          if (files[i].type != '') {
            this.fileAdd(files[i]);
          } else {
            //文件夹处理
            this.folders(fileList.items[i]);
          }
        }
      },
      //文件夹处理
      folders(files) {
        let _this = this;
        //判断是否为原生file
        if (files.kind) {
          files = files.webkitGetAsEntry();
        }
        files.createReader().readEntries(function (file) {
          for (let i = 0; i < file.length; i++) {
            if (file[i].isFile) {
              _this.foldersAdd(file[i]);
            } else {
              _this.folders(file[i]);
            }
          }
        })
      },
      foldersAdd(entry) {
        let _this = this;
        entry.file(function (file) {
          _this.fileAdd(file)
        })
      },
      fileAdd(file) {
        if (this.limit !== undefined) this.limit--;
        if (this.limit !== undefined && this.limit < 0) return;
        //总大小
        this.size = this.size + file.size;
        //判断是否为图片文件
        if (file.type.indexOf('image') == -1) {
          file.src = 'wenjian.png';
          this.imgList.push({
            file
          });
        } else {
          let reader = new FileReader();
          let image = new Image();
          let _this=this;
          reader.readAsDataURL(file);
          reader.onload = function () {
            file.src = this.result;
            image.onload=function(){
              let width = image.width;
              let height = image.height;
              file.width=width;
              file.height=height;
              _this.imgList.push({
                file
              });
              console.log( _this.imgList);
            };
            image.src= file.src;
          }
        }
      },
      fileDel(index) {
        this.size = this.size - this.imgList[index].file.size;//总大小
        this.imgList.splice(index, 1);
        if (this.limit !== undefined) this.limit = this.imgList.length;
      },
      bytesToSize(bytes) {
        if (bytes === 0) return '0 B';
        let k = 1000, // or 1024
          sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
          i = Math.floor(Math.log(bytes) / Math.log(k));
        return (bytes / Math.pow(k, i)).toPrecision(3) + ' ' + sizes[i];
      },
      dragenter(el) {
        el.stopPropagation();
        el.preventDefault();
      },
      dragover(el) {
        el.stopPropagation();
        el.preventDefault();
      },
      drop(el) {
        el.stopPropagation();
        el.preventDefault();
        this.fileList(el.dataTransfer);
      }
    }
  
  // computed: {
  //   // 计算属性的 getter
  //   reversedMessage: function () {
  //     // `this` 指向 vm 实例
  //     return this.message.split('').reverse().join('')
  //   }
  // }
}
</script>

<style>

</style>
