<template>
  <div class="about">
    <b-jumbotron header="JAVASCRIPT 浏览器对象"
      lead="">
      <p>For more information click button</p>
      <b-btn v-b-toggle.collapseWindow
        variant="primary">window</b-btn> |

      <b-btn v-b-toggle.collapseNavigator
        variant="primary">navigator</b-btn> |

      <b-btn v-b-toggle.collapseScreen
        variant="primary">screen</b-btn> |

      <b-btn v-b-toggle.collapseLocation
        variant="primary">location</b-btn> |

      <b-btn v-b-toggle.collapseDocument
        variant="primary">document</b-btn> |

      <b-btn v-b-toggle.collapseHistory
        variant="primary">history</b-btn> |

      <b-collapse id="collapseWindow"
        class="mt-2">
        <b-card>
          <p class="card-text">window对象不但充当全局作用域，而且表示浏览器窗口。</p>
          <b-btn v-b-toggle.collapseWindow_inner
            size="sm">显示更多</b-btn>
          <b-collapse id=collapseWindow_inner
            class="mt-2">
            <b-card>
              <p>window对象有innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高。</p>
              <p>{{getWindow[0]}}</p>
              <p>{{getWindow[1]}}</p>
            </b-card>
          </b-collapse>
        </b-card>
      </b-collapse>

      <b-collapse id="collapseNavigator"
        class="mt-2">
        <b-card>
          <p class="card-text">Navigtor对象表示浏览器的信息。</p>
          <b-btn v-b-toggle.collapse1_inner
            size="sm">显示更多</b-btn>
          <b-collapse id=collapse1_inner
            class="mt-2">
            <b-card>
              <ul>
                <li v-for='item in getNavigator'
                  :key='item'>
                  {{item}}
                </li>
              </ul>
            </b-card>
          </b-collapse>
        </b-card>
      </b-collapse>

      <b-collapse id="collapseScreen"
        class="mt-2">
        <b-card>
          <p class="card-text">screen对象表示屏幕的信息</p>
          <b-btn v-b-toggle.collapseScreen_inner
            size="sm">显示更多</b-btn>
          <b-collapse id=collapseScreen_inner
            class="mt-2">
            <b-card>
              <p>{{getScreen}}</p>
            </b-card>
          </b-collapse>
        </b-card>
      </b-collapse>

      <b-collapse id="collapseLocation"
        class="mt-2">
        <b-card>
          <p class="card-text">Location对象表示当前页面的URL信息。</p>
          <b-btn v-b-toggle.collapseLocation_inner
            size="sm">显示更多</b-btn>
          <b-collapse id=collapseLocation_inner
            class="mt-2">
            <b-card>
              <ul>
                <li v-for='item in getLocation'
                  :key='item'>
                  {{item}}
                </li>
              </ul>
            </b-card>
          </b-collapse>
        </b-card>
      </b-collapse>

      <b-collapse id="collapseDocument"
        class="mt-2">
        <b-card>
          <p class="card-text">Document对象表示当前页。</p>
          <b-btn v-b-toggle.collapseDocument_inner
            size="sm">显示更多</b-btn>
          <b-collapse id=collapseDocument_inner
            class="mt-2">
            <b-card>
              <ul>
                <li v-for='item in getDocument'
                  :key='item'>
                  {{item}}
                </li>
              </ul>
            </b-card>
          </b-collapse>
        </b-card>
      </b-collapse>

      <b-collapse id="collapseHistory"
        class="mt-2">
        <b-card>
          <p class="card-text">history对象表示历史记录。</p>
          <b-btn v-b-toggle.collapseHistory_inner
            size="sm">显示更多</b-btn>
          <b-collapse id=collapseHistory_inner
            class="mt-2">
            <b-card>
              {{history.des}}
            </b-card>
          </b-collapse>
        </b-card>
      </b-collapse>

    </b-jumbotron>
    <div class="container">

    </div>
    <vue-particles color="#00ff00"
      :particleOpacity=".9"
      :particlesNumber="80"
      shapeType="circle"
      :particleSize="4"
      linesColor="#ff0000"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.6"
      :linesDistance="50"
      :moveSpeed="5"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
      clickMode="push">
    </vue-particles>
  </div>
</template>
<script>
export default {
  // beforeMounted() {
  //   init();
  // },
  computed: {
    getWindow() {
      let windowInfo = [
        `窗口内部尺寸为 ${window.innerHeight} * ${window.innerWidth}`,
        `窗口外部尺寸为 ${window.outerHeight} * ${window.outerWidth}`
      ];
      return windowInfo;
    },
    getNavigator() {
      let navigatorInfo = [
        `浏览器名称为：${navigator.appName}`,
        `浏览器版本为：${navigator.appVersion}`,
        `浏览器设置的语言为:${navigator.language}`,
        `操作系统的类型：${navigator.platform}`,
        `浏览器设置的User-Agent：${navigator.userAgent}`
      ];
      return navigatorInfo;
    },
    getScreen() {
      let screenInfo = `屏幕宽度为：${screen.width},屏幕高度为：${
        screen.height
      },屏幕颜色位数:${screen.colorDepth}`;
      return screenInfo;
    },
    getLocation() {
      let locationInfo = [
        `协议是：${location.protocol}`,
        `主机地址是：${location.host}`,
        `端口是：${location.port}`,
        `路径名是：${location.pathname}`,
        `搜索的信息是：${location.search}`,
        `哈希值是：${location.hash}`
      ];
      return locationInfo;
    },
    getDocument() {
      let documentInfo = [
        `当前页面的标题是:${document.title}`,
        `当前页面的cookis是：${document.cookie}`,
        `cookie是无协议的，所以最好设置 httpOnly，会比较安全`
      ];
      return documentInfo;
    }
  },
  data() {
    return {
      window: "",
      navigator: "",
      screen: "",
      location: "",
      document: "",
      history: { des: "history对象保存浏览器的历史记录，不推荐使用" }
    };
  },
  methods: {}
};
</script>

<style>
code {
  border: 1px solid orchid;
}
canvas {
  position: fixed;
  width: 100%;
  height: 400px;
  top: 0;
  left: 0;
  z-index: -1;
}
.about {
  height: auto;
  width: 100%;
  position: absolute;
  top: 100px;
  left: 0;
  /* color: #ff00ff; */
  text-align: center;
}
.card-body {
  clear: both;
  text-align: center;
}
</style>

