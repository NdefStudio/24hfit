<template>
  <div style="height:100%">
    <div class='bigtime'>{{time}}</div>
    <div class="bigbox">
      <flexbox class="routine-column"
               :gutter="0"
               v-for="(list, index) in routinelist"
               :key="index">
        <flexbox-item :span="1/3"
                      v-for="routine in list"
                      :key="routine"
                      @click.native="onClickRoutine(routine)">
          <div :class="routine.name==selected?'selected-routine-box':'routine-box'">
            <span v-html="routine.icon"
                  :style="{color: routine.color}"></span>
            <br>
            <span :style="{fontSize: routine.name.length > 12 ? '12px' : ''}">{{routine.name}}</span>
          </div>
        </flexbox-item>
      </flexbox>
    </div>
  </div>
</template>

<script>
import { Flexbox, FlexboxItem } from 'vux'

export default {
  components: {
    Flexbox,
    FlexboxItem
  },
  mounted() {
    /*页面载入时从后台获取现在记录的状态（正在进行的routine*/
    this.selected = '睡眠'
  },
  created() {
    setInterval(this.getTime, 500)
  },
  methods: {
    getTime: function() {
      var _this = this
      let yy = new Date().getFullYear()
      let mm = new Date().getMonth() + 1
      let dd = new Date().getDate()
      let hh = new Date().getHours()
      let mf =
        new Date().getMinutes() < 10
          ? '0' + new Date().getMinutes()
          : new Date().getMinutes()
      let ss =
        new Date().getSeconds() < 10
          ? '0' + new Date().getSeconds()
          : new Date().getSeconds()
      _this.time = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + mf + ':' + ss
    },
    onClickRoutine(routine) {
      /*
      在点击某一个routine之后，会将其高亮
      需要传递三个信息：
      是否存在这个操作所取消的routine
      新的routine名称
      这个操作的时间
      */

      this.selected = routine.name
      //在这里发送请求
    },
    split(array) {
      let chunks = []
      let count = Math.ceil(array.length / 3)
      while (count > 0) {
        chunks.push(array.slice((count - 1) * 3, count * 3))
        count--
      }
      chunks = chunks.reverse()
      const lastList = chunks[chunks.length - 1]
      const lastLength = lastList.length
      if (lastLength < 3) {
        for (let i = 0; i < 3 - lastLength; i++) {
          lastList.push({
            name: '----',
            icon: ''
          })
        }
      }
      //console.log(chunks)
      return chunks
    }
  },
  data() {
    return {
      time: '',
      selected: '',
      routinelist: this.split([
        { name: '睡眠', icon: 'bla1' },
        { name: '学习', icon: 'bla1' },
        { name: '工作', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '走路', icon: 'bla1' },
        { name: '自由思考', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '跑步', icon: 'bla1' },
        { name: '跳绳', icon: 'bla1' },
        { name: '走路', icon: 'bla1' },
        { name: '自由思考', icon: 'bla1' }
      ])
    }
  }
}
</script>

<style>
.bigtime {
  text-align: center;
  margin: 7%;
  margin-top: 40px;
  font-size: 50px;
  background-color: #fff;
}
.bigbox {
  padding-left: 20px;
  padding-right: 20px;
  font-size: 20px;
  height: 70%;
  overflow: scroll;
  -webkit-overflow-scrolling: touch;
}
.routine-box {
  text-align: center;
  margin-left: 5px;
  margin-right: 5px;
  background-color: #fff;
}
.selected-routine-box {
  text-align: center;
  margin-left: 5px;
  margin-right: 5px;
  background-color: #50c6f1;
  color: azure;
}
.routine-column {
  margin-bottom: 10px;
}
</style>