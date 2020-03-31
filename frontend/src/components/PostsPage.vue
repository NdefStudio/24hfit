<template>
  <div>
    <view-box ref="viewBox"
              :body-padding-top="isShowNav ? '46px' : '0'"
              body-padding-bottom="55px">
      <timeline class="scrollbox">
        <timeline-item v-for="(item,index) in allposts "
                       :key="index">
          <div class="postitem">
            <h3>{{item.title}}</h3>
            <p class="timetext">{{item.time}}</p>
            <p>{{item.content}}</p>
          </div>
        </timeline-item>
      </timeline>
    </view-box>
  </div>
</template>

<script>
import { Timeline, TimelineItem } from 'vux'

export default {
  components: { Timeline, TimelineItem },
  data() {
    return {
      allposts: []
    }
  },
  methods: {
    testzsbd: function(q) {
      var str = ''
      for (var i = 0; i < q; i++) str += 'zsbdzsbd'
      return str
    },
    getTime: function() {
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
      return yy + '-' + mm + '-' + dd + ' ' + hh + ':' + mf + ':' + ss
    },
    getPosts: function() {
      this.$axios
        .get(this.global.apiserver + 'psts', {
          params: {
            id: this.global.id
          }
        })
        .then(response => {
          console.log(response)
          this.allposts = response.data.allposts
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    // 获取所有日志的请求
    // 单个日志应至少含有时间和内容
    // 这里先造一个
    // 造完了，参见APIS.md

    this.getPosts()
  }
}
</script>

<style>
.timetext {
  color: #888;
  font-size: 0.8rem;
}
.postitem {
  background-color: #ffffff81;
}
.scrollbox {
  word-wrap: break-word;
  height: 100%;
  margin-top: 25px;
}
</style>