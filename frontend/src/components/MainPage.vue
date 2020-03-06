<template>
  <div style="height:100%">
    <drawer width="200px;"
            :show.sync="drawerVisibility"
            show-mode="overlay"
            placement="left"
            :drawer-style="{'background-color':'#35495e', width: '150px'}">

      <!-- drawer content -->
      <div slot="drawer">
        <group title='快速操作'>
          <cell title="添加事务"></cell>
          <cell title="现在心情"></cell>
          <cell title="分享"></cell>
        </group>
      </div>
      <view-box ref="viewBox"
                body-padding-bottom="55px">
        <x-header slot="header"
                  style="width:100%;position:fixed;
              left:0;top:0;z-index:100;background-color:#43c9db;">
          <span>24hFit</span>
          <x-icon slot="overwrite-left"
                  type="navicon"
                  size="35"
                  style="fill:#fff;position:relative;top:-8px;left:-3px;"
                  @click="onClickDrawer"></x-icon>
        </x-header>
        <!--    <tabbar @on-index-change="onIndexChange">
      <tabbar-item>
        <img slot="icon"
             src="../assets/demo/icon_nav_button.png">
        <img slot="icon-active"
             src="../assets/demo/icon_nav_msg.png">
        <span slot="label">one</span>
      </tabbar-item>
      <tabbar-item>
        <img slot="icon"
             src="../assets/demo/icon_nav_article.png">
        <img slot="icon-active"
             src="../assets/demo/icon_nav_cell.png">
        <span slot="label">two</span>
      </tabbar-item>
    </tabbar>
    -->
        <keep-alive>
          <router-view class="routerv"></router-view>
        </keep-alive>
        <tabbar style="width:100%;position:fixed;
              left:0;z-index:100;"
                @on-index-change="onTabChange">
          <tabbar-item selected
                       :link="{path:`/main/${id}/routine`}">
            <span slot="label">事务</span>
          </tabbar-item>
          <tabbar-item :link="{path:`/main/${id}/posts`}">
            <span slot="label">帖子</span>
          </tabbar-item>
          <tabbar-item :link="{path:`/main/${id}/my`}">
            <span slot="label">我</span>
          </tabbar-item>
        </tabbar>
      </view-box>
    </drawer>
  </div>
</template>

<script>
import { XHeader, Tabbar, TabbarItem, Drawer, Group, Cell, ViewBox } from 'vux'

export default {
  components: {
    XHeader,
    Tabbar,
    TabbarItem,
    Drawer,
    Group,
    Cell,
    ViewBox
  },
  data() {
    return {
      drawerVisibility: false,
      id: this.$route.params.id
    }
  },
  methods: {
    onClickDrawer() {
      this.drawerVisibility = !this.drawerVisibility
      console.log(this.draweropen)
    },
    onTabChange(oldindex, newindex) {
      console.log(oldindex, newindex)
    }
  }
}
</script>

<style>
.routerv {
  top: 20px;
  bottom: 90px;
  height: 90%;
  position: fixed;
  width: 100%;
  overflow: scroll;
  -webkit-overflow-scrolling: touch;
}
</style>