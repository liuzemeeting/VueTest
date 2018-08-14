1.html模板
<p v-text="value"></p>等同于<p>{{ value }}</p>
其中<p v-html="value"></p>会解析元素中的html标签元素
原生的html：双大括号输出的文本，不会解析html标签。也就是说当实例的data为html标签时，不能解析而是直接输出出来。此时如想要解析，可使用v-html="value"代替。
2.点击事件(v-bind 和 v-on 这两个最常用的指令)
v-bind 缩写
<!-- 完整语法 -->
<a v-bind:href="url">...</a>
<!-- 缩写 -->
<a :href="url">...</a>
v-on 缩写
<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>
<!-- 缩写 -->
<a @click="doSomething">...</a>
