(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1de4847e"],{"129f":function(t,e){t.exports=Object.is||function(t,e){return t===e?0!==t||1/t===1/e:t!=t&&e!=e}},5118:function(t,e,s){(function(t){var a="undefined"!==typeof t&&t||"undefined"!==typeof self&&self||window,n=Function.prototype.apply;function i(t,e){this._id=t,this._clearFn=e}e.setTimeout=function(){return new i(n.call(setTimeout,a,arguments),clearTimeout)},e.setInterval=function(){return new i(n.call(setInterval,a,arguments),clearInterval)},e.clearTimeout=e.clearInterval=function(t){t&&t.close()},i.prototype.unref=i.prototype.ref=function(){},i.prototype.close=function(){this._clearFn.call(a,this._id)},e.enroll=function(t,e){clearTimeout(t._idleTimeoutId),t._idleTimeout=e},e.unenroll=function(t){clearTimeout(t._idleTimeoutId),t._idleTimeout=-1},e._unrefActive=e.active=function(t){clearTimeout(t._idleTimeoutId);var e=t._idleTimeout;e>=0&&(t._idleTimeoutId=setTimeout((function(){t._onTimeout&&t._onTimeout()}),e))},s("6017"),e.setImmediate="undefined"!==typeof self&&self.setImmediate||"undefined"!==typeof t&&t.setImmediate||this&&this.setImmediate,e.clearImmediate="undefined"!==typeof self&&self.clearImmediate||"undefined"!==typeof t&&t.clearImmediate||this&&this.clearImmediate}).call(this,s("c8ba"))},6017:function(t,e,s){(function(t,e){(function(t,s){"use strict";if(!t.setImmediate){var a,n=1,i={},o=!1,r=t.document,l=Object.getPrototypeOf&&Object.getPrototypeOf(t);l=l&&l.setTimeout?l:t,"[object process]"==={}.toString.call(t.process)?g():p()?h():t.MessageChannel?f():r&&"onreadystatechange"in r.createElement("script")?v():b(),l.setImmediate=c,l.clearImmediate=u}function c(t){"function"!==typeof t&&(t=new Function(""+t));for(var e=new Array(arguments.length-1),s=0;s<e.length;s++)e[s]=arguments[s+1];var o={callback:t,args:e};return i[n]=o,a(n),n++}function u(t){delete i[t]}function d(t){var e=t.callback,a=t.args;switch(a.length){case 0:e();break;case 1:e(a[0]);break;case 2:e(a[0],a[1]);break;case 3:e(a[0],a[1],a[2]);break;default:e.apply(s,a);break}}function m(t){if(o)setTimeout(m,0,t);else{var e=i[t];if(e){o=!0;try{d(e)}finally{u(t),o=!1}}}}function g(){a=function(t){e.nextTick((function(){m(t)}))}}function p(){if(t.postMessage&&!t.importScripts){var e=!0,s=t.onmessage;return t.onmessage=function(){e=!1},t.postMessage("","*"),t.onmessage=s,e}}function h(){var e="setImmediate$"+Math.random()+"$",s=function(s){s.source===t&&"string"===typeof s.data&&0===s.data.indexOf(e)&&m(+s.data.slice(e.length))};t.addEventListener?t.addEventListener("message",s,!1):t.attachEvent("onmessage",s),a=function(s){t.postMessage(e+s,"*")}}function f(){var t=new MessageChannel;t.port1.onmessage=function(t){var e=t.data;m(e)},a=function(e){t.port2.postMessage(e)}}function v(){var t=r.documentElement;a=function(e){var s=r.createElement("script");s.onreadystatechange=function(){m(e),s.onreadystatechange=null,t.removeChild(s),s=null},t.appendChild(s)}}function b(){a=function(t){setTimeout(m,0,t)}}})("undefined"===typeof self?"undefined"===typeof t?this:t:self)}).call(this,s("c8ba"),s("4362"))},"841c":function(t,e,s){"use strict";var a=s("d784"),n=s("825a"),i=s("1d80"),o=s("129f"),r=s("14c3");a("search",1,(function(t,e,s){return[function(e){var s=i(this),a=void 0==e?void 0:e[t];return void 0!==a?a.call(e,s):new RegExp(e)[t](String(s))},function(t){var a=s(e,t,this);if(a.done)return a.value;var i=n(t),l=String(this),c=i.lastIndex;o(c,0)||(i.lastIndex=0);var u=r(i,l);return o(i.lastIndex,c)||(i.lastIndex=c),null===u?-1:u.index}]}))},"857a":function(t,e,s){var a=s("1d80"),n=/"/g;t.exports=function(t,e,s,i){var o=String(a(t)),r="<"+e;return""!==s&&(r+=" "+s+'="'+String(i).replace(n,"&quot;")+'"'),r+">"+o+"</"+e+">"}},9911:function(t,e,s){"use strict";var a=s("23e7"),n=s("857a"),i=s("af03");a({target:"String",proto:!0,forced:i("link")},{link:function(t){return n(this,"a","href",t)}})},"99af":function(t,e,s){"use strict";var a=s("23e7"),n=s("d039"),i=s("e8b5"),o=s("861d"),r=s("7b0b"),l=s("50c4"),c=s("8418"),u=s("65f0"),d=s("1dde"),m=s("b622"),g=s("2d00"),p=m("isConcatSpreadable"),h=9007199254740991,f="Maximum allowed index exceeded",v=g>=51||!n((function(){var t=[];return t[p]=!1,t.concat()[0]!==t})),b=d("concat"),x=function(t){if(!o(t))return!1;var e=t[p];return void 0!==e?!!e:i(t)},_=!v||!b;a({target:"Array",proto:!0,forced:_},{concat:function(t){var e,s,a,n,i,o=r(this),d=u(o,0),m=0;for(e=-1,a=arguments.length;e<a;e++)if(i=-1===e?o:arguments[e],x(i)){if(n=l(i.length),m+n>h)throw TypeError(f);for(s=0;s<n;s++,m++)s in i&&c(d,m,i[s])}else{if(m>=h)throw TypeError(f);c(d,m++,i)}return d.length=m,d}})},"9f84":function(t,e,s){"use strict";s.r(e);var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"disable-text-selection"},[t.isLoad?s("todo-application-menu",{attrs:{loadFiltersR:t.loadFiltersR,items:t.items,categories:t.categories,labels:t.labels,categoryID:t.categoryID}}):t._e(),t._v(" "),s("b-row",{staticClass:"app-row survey-app"},[s("b-colxx",{staticClass:"disable-text-selection"},[s("list-page-heading",{attrs:{title:t.title,selectAll:t.selectAll,isSelectedAll:t.isSelectedAll,isAnyItemSelected:t.isAnyItemSelected,keymap:t.keymap,displayMode:t.displayMode,changeDisplayMode:t.changeDisplayMode,changeOrderBy:t.changeOrderBy,changePageSize:t.changePageSize,sort:t.sort,searchChange:t.searchChange,from:t.from,to:t.to,total:t.total,perPage:t.perPage,categoryID:t.categoryID,loadItems:t.loadItems,currentUser:t.currentUser}}),t._v(" "),t.isLoad?[s("list-page-listing",{attrs:{displayMode:t.displayMode,items:t.items,selectedItems:t.selectedItems,toggleItem:t.toggleItem,lastPage:t.lastPage,perPage:t.perPage,page:t.page,changePage:t.changePage,handleContextMenu:t.handleContextMenu,loadItems:t.loadItems,onContextMenuAction:t.onContextMenuAction,currentUser:t.currentUser}})]:[s("div",{staticClass:"loading"})]],2)],1)],1)},n=[],i=(s("99af"),s("4de4"),s("caad"),s("d81d"),s("fb6a"),s("b0c0"),s("d3b7"),s("ac1f"),s("25f0"),s("2532"),s("841c"),s("5530")),o=s("2909"),r=s("bc3a"),l=s.n(r),c=s("2b47"),u=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("b-row",[s("b-colxx",{attrs:{xxs:"12"}},[s("h1",[t._v(t._s(t.title))]),t._v(" "),s("div",{staticClass:"top-right-button-container"},[null!=t.currentUser?s("b-button",{directives:[{name:"b-modal",rawName:"v-b-modal.modalright",modifiers:{modalright:!0}}],staticClass:"top-right-button",attrs:{variant:"primary",size:"lg"}},[t._v(t._s(t.$t("pages.add-new")))]):t._e()],1),t._v(" "),s("add-new-modal",{attrs:{categoryID:t.categoryID},on:{update:t.loadItems}}),t._v(" "),s("div",{staticClass:"mb-2 mt-2"},[s("b-button",{directives:[{name:"b-toggle",rawName:"v-b-toggle.displayOptions",modifiers:{displayOptions:!0}}],staticClass:"pt-0 pl-0 d-inline-block d-md-none",attrs:{variant:"empty"}},[t._v("\n        "+t._s(t.$t("pages.display-options"))+"\n        "),s("i",{staticClass:"simple-icon-arrow-down align-middle"})]),t._v(" "),s("b-collapse",{staticClass:"d-md-block",attrs:{id:"displayOptions"}},[s("div",{staticClass:"d-block d-md-inline-block pt-1"},[s("b-dropdown",{staticClass:"mr-1 float-md-left btn-group",attrs:{id:"ddown1",text:t.$t("pages.orderby")+" "+t.sort.label,variant:"outline-dark",size:"xs"}},t._l(t.sortOptions,(function(e,a){return s("b-dropdown-item",{key:a,on:{click:function(s){return t.changeOrderBy(e)}}},[t._v(t._s(e.label))])})),1),t._v(" "),s("div",{staticClass:"search-sm d-inline-block float-md-left mr-1 align-top"},[s("b-input",{attrs:{placeholder:t.$t("menu.search")},on:{input:function(e){return t.searchChange(e)}}})],1)],1)])],1),t._v(" "),s("div",{staticClass:"separator mb-5"})],1)],1)},d=[],m=s("f7d9"),g=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("b-modal",{ref:"modalright",attrs:{id:"modalright",title:"Add New Resource",size:"md","hide-footer":""}},[s("b-card",{attrs:{"no-body":""}},[s("b-card-body",{staticClass:"wizard wizard-default"},[s("form-wizard",{attrs:{"last-step-end":!0}},[s("tab",{attrs:{name:"Properties",selected:!0}},[s("div",{staticClass:"wizard-basic-step"},[s("b-form",[s("b-form-group",{attrs:{label:"Title:"}},[s("b-form-input",{attrs:{placeholder:"enter title of resource"},model:{value:t.newItem.title,callback:function(e){t.$set(t.newItem,"title",e)},expression:"newItem.title"}})],1),t._v(" "),s("b-form-group",{attrs:{label:"Link:"}},[s("b-form-input",{attrs:{placeholder:"enter link to resource"},model:{value:t.newItem.link,callback:function(e){t.$set(t.newItem,"link",e)},expression:"newItem.link"}})],1),t._v(" "),s("b-form-group",{attrs:{label:"Description: (optional)"}},[s("b-textarea",{attrs:{rows:4,"max-rows":2,placeholder:"enter description of resource"},model:{value:t.newItem.description,callback:function(e){t.$set(t.newItem,"description",e)},expression:"newItem.description"}})],1)],1)],1)]),t._v(" "),s("tab",{attrs:{name:"tags",selected:!1}},[s("div",{staticClass:"wizard-basic-step"},[t._l(t.filters,(function(e,a){return s("div",{key:a},[s("label",[t._v(t._s(e.title))]),t._v(" "),s("b-form-checkbox-group",{staticClass:"list-unstyled mb-4",attrs:{stacked:""},model:{value:t.selectedFilters,callback:function(e){t.selectedFilters=e},expression:"selectedFilters"}},t._l(e.tags,(function(a,n){return s("b-form-checkbox",{key:n,attrs:{name:e.title,value:a.id}},[t._v(t._s(a.title))])})),1)],1)})),t._v(" "),t._l(t.subCategories,(function(e,a){return s("div",{key:a},[s("label",[t._v(t._s(e.title))]),t._v(" "),s("b-form-checkbox-group",{staticClass:"list-unstyled mb-4",attrs:{stacked:""},model:{value:t.selectedsubCategories,callback:function(e){t.selectedsubCategories=e},expression:"selectedsubCategories"}},t._l(e.tags,(function(a,n){return s("b-form-checkbox",{key:n,attrs:{name:e.title,value:a.id}},[t._v(t._s(a.title))])})),1)],1)}))],2)]),t._v(" "),s("tab",{attrs:{type:"done"}},[s("div",{staticClass:"wizard-basic-step text-center"},[s("h2",{staticClass:"mb-2"},[t._v("Are you sure you want to submit this resource?")]),t._v(" "),s("button",{staticClass:"btn btn-primary",attrs:{type:"button"},on:{click:t.addNewItem}},[t._v("\n              submit\n            ")])])])],1)],1)],1)],1)},p=[],h=(s("a4d3"),s("e01a"),s("9911"),s("4a7a")),f=s.n(h),v=(s("6dfc"),s("99c7")),b=(s("a753"),s("8096"),s("14e1"),s("92c3")),x=s.n(b),_=s("2f62"),y=(s("953d"),s("c033")),w={components:{"v-select":f.a,Tab:v["a"],FormWizard:y["a"],"vue-dropzone":x.a},props:["categoryID"],data:function(){return{tags:[],filters:[],subCategories:[],filter:[],selectedFilters:[],selectedsubCategories:[],checkBoxTags:[{text:"free",value:1},{text:"paid",value:2},{text:"beginner",value:3},{text:"advanced",value:4}],newItem:{title:"",link:"",description:"",tags:[]},error:"",mainImageDropzoneOptions:{url:"".concat(c["c"],"/upload"),thumbnailHeight:150,maxFilesize:2,maxFiles:1,acceptedFiles:"image/*",dictDefaultMessage:"drop image of tutorial in this box",previewTemplate:this.dropzoneTemplate()}}},computed:Object(i["a"])({},Object(_["c"])({currentUser:"currentUser",menuType:"getMenuType",menuClickCount:"getMenuClickCount",selectedMenuHasSubItems:"getSelectedMenuHasSubItems"})),methods:{loadFilters:function(){var t=this;console.log(),l.a.get(c["b"]+"ListTags/").then((function(t){return console.log("tags list"),console.log(t),t.data})).then((function(e){t.tags=e;for(var s=0;s<e.length;s++)t.filter.includes(e[s].type)||t.filter.push(e[s].type);for(var a=0;a<t.filter.length;a++){var n=[];for(s=0;s<t.tags.length;s++)t.filter[a]==t.tags[s].type&&n.push(t.tags[s]);t.filters.push({title:t.filter[a],tags:n})}console.log("filters"),console.log(t.filters)}))},loadSubCategory:function(){var t=this,e={categoryId:this.categoryID};l.a.post(c["b"]+"subcategoryList/",e).then((function(t){return t.data})).then((function(e){t.subCategories.push({title:"cubcategory",tags:e}),console.log(t.filters)}))},addNewItem:function(){var t=this,e={submitter:this.currentUser.id,category:this.categoryID,title:this.newItem.title,link:this.newItem.link,description:this.newItem.description,tags:this.selectedFilters,subs:this.selectedsubCategories};l.a.post("".concat(c["b"],"createResource/"),e).then((function(t){return t.data})).then((function(e){console.log("add new resource"),console.log(e),t.hideModal("modalright"),t.newItem.title="",t.newItem.link="",t.newItem.description="",t.newItem.tags=[],t.$emit("update")}))},hideModal:function(t){this.$refs[t].hide()},dropzoneTemplate:function(){return'<div class="dz-preview dz-file-preview mb-3">\n                <div class="d-flex flex-row "> \n                  <div class="p-0 w-30 position-relative">\n                    <div class="dz-error-mark"><span><i></i>  </span></div>\n                    <div class="dz-success-mark"><span><i></i></span></div>\n                    <div class="preview-container">\n                      <img data-dz-thumbnail class="img-thumbnail border-0" />\n                      <i class="simple-icon-doc preview-icon"></i>\n                    </div>\n                  </div>\n                  <div class="pl-3 pt-2 pr-2 pb-1 w-40 dz-details position-relative m-2">\n                    <div> <span data-dz-name style="direction:ltr" /> </div>\n                    <div class="text-primary text-extra-small" style="direction:ltr" data-dz-size /> </div>\n                    <div class="dz-progress"><span class="dz-upload" data-dz-uploadprogress></span></div>\n                    <div class="dz-error-message"><span data-dz-errormessage></span></div>\n                  </div>\n                  <a href="#" class="remove" data-dz-remove> <i class="glyph-icon simple-icon-trash"></i> </a>\n                </div>\n              </div>\n        '},mainImageUploadSuccess:function(t,e){this.newItem.mainImage=e.url},mainImageDeleteFile:function(t,e,s){console.log(t),console.log(e),console.log(s)}},mounted:function(){this.loadSubCategory(),this.loadFilters()}},k=w,C=s("2877"),I=Object(C["a"])(k,g,p,!1,null,null,null),M=I.exports,O={components:{"data-list-icon":m["a"],"thumb-list-icon":m["e"],"image-list-icon":m["b"],"add-new-modal":M},props:["title","selectAll","isSelectedAll","isAnyItemSelected","keymap","displayMode","changeDisplayMode","changeOrderBy","changePageSize","sort","searchChange","from","to","total","perPage","categoryID","currentUser","loadItems"],data:function(){return{categories:[{label:"Cakes",value:"Cakes"},{label:"Cupcakes",value:"Cupcakes"},{label:"Desserts",value:"Desserts"}],statuses:[{text:"ON HOLD",value:"ON HOLD"},{text:"PROCESSED",value:"PROCESSED"}],sortOptions:[{column:"Oldest",label:"Oldest"},{column:"Newest",label:"Newest"},{column:"Rating",label:"Rating"}],pageSizes:[4,8,12]}},methods:{searchChange2:function(t){console.log("in search"),console.log(t)}}},A=O,D=Object(C["a"])(A,u,d,!1,null,null,null),S=D.exports,H=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",["image"===t.displayMode?s("b-row",{key:"image"},t._l(t.items,(function(e,a){return s("b-colxx",{key:a,staticClass:"mb-3",attrs:{sm:"6",lg:"4",xl:"3",id:e.resource_id}},[s("image-list-item",{directives:[{name:"contextmenu",rawName:"v-contextmenu:contextmenu",arg:"contextmenu"}],key:e.resource_id,attrs:{data:e,"selected-items":t.selectedItems,loadItems:t.loadItems,currentUser:t.currentUser},on:{"toggle-item":t.toggleItem}})],1)})),1):"thumb"===t.displayMode?s("b-row",{key:"thumb"},t._l(t.items,(function(e,a){return s("b-colxx",{key:a,staticClass:"mb-3",attrs:{xxs:"12",id:e.resource_id}},[s("thumb-list-item",{directives:[{name:"contextmenu",rawName:"v-contextmenu:contextmenu",arg:"contextmenu"}],key:e.resource_id,attrs:{data:e,"selected-items":t.selectedItems},on:{"toggle-item":t.toggleItem}})],1)})),1):"list"===t.displayMode?s("b-row",{key:"list"},t._l(t.items,(function(e,a){return s("b-colxx",{key:a,staticClass:"mb-3",attrs:{xxs:"12",id:e.resource_id}},[s("data-list-item",{directives:[{name:"contextmenu",rawName:"v-contextmenu:contextmenu",arg:"contextmenu"}],key:e.resource_id,attrs:{data:e,"selected-items":t.selectedItems},on:{"toggle-item":t.toggleItem}})],1)})),1):t._e(),t._v(" "),t.lastPage>1?s("b-row",[s("b-colxx",{attrs:{xxs:"12"}},[s("b-pagination-nav",{attrs:{"number-of-pages":t.lastPage,"link-gen":t.linkGen,value:t.page,"per-page":t.perPage,align:"center"},on:{change:function(e){return t.changePage(e)}},scopedSlots:t._u([{key:"next-text",fn:function(){return[s("i",{staticClass:"simple-icon-arrow-right"})]},proxy:!0},{key:"prev-text",fn:function(){return[s("i",{staticClass:"simple-icon-arrow-left"})]},proxy:!0},{key:"first-text",fn:function(){return[s("i",{staticClass:"simple-icon-control-start"})]},proxy:!0},{key:"last-text",fn:function(){return[s("i",{staticClass:"simple-icon-control-end"})]},proxy:!0}],null,!1,2104427419)})],1)],1):t._e(),t._v(" "),s("v-contextmenu",{ref:"contextmenu",on:{contextmenu:t.handleContextMenu}},[s("v-contextmenu-item",{on:{click:function(e){return t.onContextMenuAction("copy")}}},[s("i",{staticClass:"simple-icon-docs"}),t._v(" "),s("span",[t._v("Copy")])]),t._v(" "),s("v-contextmenu-item",{on:{click:function(e){return t.onContextMenuAction("move-to-archive")}}},[s("i",{staticClass:"simple-icon-drawer"}),t._v(" "),s("span",[t._v("Move to archive")])]),t._v(" "),s("v-contextmenu-item",{on:{click:function(e){return t.onContextMenuAction("delete")}}},[s("i",{staticClass:"simple-icon-trash"}),t._v(" "),s("span",[t._v("Delete")])])],1)],1)},z=[],E=s("f8b6"),T=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("router-link",{staticClass:"w-40 w-sm-100",attrs:{to:"/app/resourceDetail"}},[s("b-card",{class:{"d-flex flex-row":!0,active:t.selectedItems.includes(t.data.id)},attrs:{"no-body":""}},[s("img",{staticClass:"list-thumbnail responsive border-0",attrs:{src:t.data.img,alt:t.data.title}}),t._v(" "),s("div",{staticClass:"pl-2 d-flex flex-grow-1 min-width-zero"},[s("div",{staticClass:"card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center"},[s("p",{staticClass:"list-item-heading mb-0 truncate"},[t._v(t._s(t.data.title))]),t._v(" "),s("p",{staticClass:"mb-0 text-muted text-small w-15 w-sm-100"},[t._v("\n          "+t._s(t.data.category)+"\n        ")]),t._v(" "),s("p",{staticClass:"mb-0 text-muted text-small w-15 w-sm-100"},[t._v("\n          "+t._s(t.data.date)+"\n        ")]),t._v(" "),s("div",{staticClass:"w-15 w-sm-100"},[s("b-badge",{attrs:{pill:"",variant:t.data.statusColor}},[t._v(t._s(t.data.status))])],1)])])])],1)},P=[],$={props:["data","selectedItems"],methods:{toggleItem:function(t,e){this.$emit("toggle-item",t,e)}}},F=$,U=Object(C["a"])(F,T,P,!1,null,null,null),j=U.exports,L=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("router-link",{staticClass:"w-40 w-sm-100",attrs:{to:"/app/resourceDetail"}},[s("b-card",{class:{"d-flex flex-row":!0,active:t.selectedItems.includes(t.data.id)},attrs:{"no-body":""}},[s("div",{staticClass:"pl-2 d-flex flex-grow-1 min-width-zero"},[s("div",{staticClass:"card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center"},[s("p",{staticClass:"list-item-heading mb-0 truncate"},[t._v(t._s(t.data.title))]),t._v(" "),s("p",{staticClass:"mb-0 text-muted text-small w-15 w-sm-100"},[t._v("\n          "+t._s(t.data.category)+"\n        ")]),t._v(" "),s("p",{staticClass:"mb-0 text-muted text-small w-15 w-sm-100"},[t._v("\n          "+t._s(t.data.date)+"\n        ")]),t._v(" "),s("div",{staticClass:"w-15 w-sm-100"},[s("b-badge",{attrs:{pill:"",variant:t.data.statusColor}},[t._v(t._s(t.data.status))])],1)])])])],1)},V=[],B={props:["data","selectedItems"],methods:{toggleItem:function(t,e){this.$emit("toggle-item",t,e)}}},R=B,N=Object(C["a"])(R,L,V,!1,null,null,null),Z=N.exports,J={components:{"image-list-item":E["a"],"thumb-list-item":j,"data-list-item":Z},props:["displayMode","items","loadItems","selectedItems","toggleItem","lastPage","perPage","page","changePage","handleContextMenu","onContextMenuAction","currentUser"],methods:{linkGen:function(t){return"#page-"+t}}},G=J,K=Object(C["a"])(G,H,z,!1,null,null,null),Y=K.exports,q=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("application-menu",[s("vue-perfect-scrollbar",{attrs:{settings:{suppressScrollX:!0,wheelPropagation:!1}}},[s("div",{staticClass:"p-4"},[t._l(t.filters,(function(e,a){return s("div",[s("label",[t._v(t._s(e.title))]),t._v(" "),s("b-form-checkbox-group",{staticClass:"list-unstyled mb-4",attrs:{stacked:""},model:{value:t.selectedFilters,callback:function(e){t.selectedFilters=e},expression:"selectedFilters"}},t._l(e.tags,(function(a,n){return s("b-form-checkbox",{attrs:{name:e.title,value:a.id}},[t._v(t._s(a.title))])})),1)],1)})),t._v(" "),t._l(t.subCategories,(function(e,a){return s("div",[s("label",[t._v(t._s(e.title))]),t._v(" "),s("b-form-checkbox-group",{staticClass:"list-unstyled mb-4",attrs:{stacked:""},model:{value:t.selectedsubCategories,callback:function(e){t.selectedsubCategories=e},expression:"selectedsubCategories"}},t._l(e.tags,(function(a,n){return s("b-form-checkbox",{attrs:{name:e.title,value:a.id}},[t._v(t._s(a.title))])})),1)],1)}))],2)])],1)},W=[],X=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{class:{"app-menu":!0,shown:t.isOpen},on:{mouseenter:function(e){t.isMenuOver=!0},mouseleave:function(e){t.isMenuOver=!1}}},[t._t("default"),t._v(" "),s("a",{staticClass:"app-menu-button d-inline-block d-xl-none",on:{click:function(e){return e.preventDefault(),t.toggle(e)}}},[s("i",{staticClass:"simple-icon-options"})])],2)},Q=[],tt=s("5118"),et={data:function(){return{isOpen:!1,isMenuOver:!1}},methods:{addEvents:function(){document.addEventListener("click",this.handleDocumentClick),document.addEventListener("touchstart",this.handleDocumentClick)},removeEvents:function(){document.removeEventListener("click",this.handleDocumentClick),document.removeEventListener("touchstart",this.handleDocumentClick)},handleDocumentClick:function(t){this.isMenuOver||this.toggle()},toggle:function(){this.isOpen=!this.isOpen}},watch:{isOpen:function(t){var e=this;t?(Object(tt["setTimeout"])((function(){e.$emit("show")}),300),this.addEvents()):this.removeEvents()}},beforeDestroy:function(){this.removeEvents()}},st=et,at=Object(C["a"])(st,X,Q,!1,null,null,null),nt=at.exports,it={props:["categories","labels","items","categoryID","loadFiltersR"],components:{"application-menu":nt},data:function(){return{tags:[],filters:[],subCategories:[],filter:[],selectedFilters:[],selectedsubCategories:[],options1:[{text:"paid",value:"first"},{text:"free",value:"second"}],options2:[{text:"video",value:"first"},{text:"book",value:"second"}],options3:[{text:"beginner",value:"first"},{text:"advanced",value:"second"}]}},watch:{selectedFilters:function(){this.loadFiltersR(this.selectedFilters,this.selectedsubCategories)},selectedsubCategories:function(){this.loadFiltersR(this.selectedFilters,this.selectedsubCategories)}},methods:{loadFilters:function(){var t=this;console.log(),l.a.get(c["b"]+"ListTags/").then((function(t){return console.log("tags list"),console.log(t),t.data})).then((function(e){t.tags=e;for(var s=0;s<e.length;s++)t.filter.includes(e[s].type)||t.filter.push(e[s].type);for(var a=0;a<t.filter.length;a++){var n=[];for(s=0;s<t.tags.length;s++)t.filter[a]==t.tags[s].type&&n.push(t.tags[s]);t.filters.push({title:t.filter[a],tags:n})}console.log("filters"),console.log(t.filters)}))},loadSubCategory:function(){var t=this,e={categoryId:this.categoryID};l.a.post(c["b"]+"subcategoryList/",e).then((function(t){return t.data})).then((function(e){t.subCategories.push({title:"subcategory",tags:e}),console.log(t.filters)}))}},mounted:function(){document.body.classList.add("right-menu"),this.loadFilters(),this.loadSubCategory()},beforeDestroy:function(){document.body.classList.remove("right-menu")}},ot=it,rt=ot,lt=Object(C["a"])(rt,q,W,!1,null,null,null),ct=lt.exports,ut={components:{"list-page-heading":S,"list-page-listing":Y,"todo-application-menu":ct},data:function(){return{title:"",resourceList:[],isLoad:!1,apiBase:c["c"]+"/cakes/fordatatable",displayMode:"image",sort:{column:"Rating",label:"Rating"},page:1,categoryID:this.$route.params.id,perPage:4,search:"",from:0,to:0,total:0,lastPage:0,items:[],selectedItems:[],categories:[{label:"Free",value:"Free"},{label:"Beginner",value:"Beginner"},{label:"Book",value:"Book"},{label:"Python3",value:"Python3"}],labels:[{label:"JAVA",value:"JAVA",color:"secondary"},{label:"PAID",value:"PAID",color:"primary"},{label:"ADVANCED",value:"ADVANCED",color:"info"}]}},methods:{loadFiltersR:function(t,e){var s=this,a={categoryId:this.$route.params.id,tags:t,subcategories:e,personId:null};null!=this.currentUser&&(a.personId=this.currentUser.id),l.a.post(c["b"]+"filterResourceList/",a).then((function(t){return console.log("resource list"),console.log(t),t.data})).then((function(t){s.items=t,s.isLoad=!0,console.log(t)}))},loadItems:function(){var t=this;console.log("load items"),console.log(this.$route.params),console.log(this.$route.params.id);var e={categoryId:this.$route.params.id,personId:null},s="";null!=this.currentUser&&(e.personId=this.currentUser.id),"Rating"==this.sort.label&&(s="orderbyLikeResourceList/"),"Oldest"==this.sort.label&&(s="resourceList/"),"Newest"==this.sort.label&&(s="newstResourceList/"),l.a.post(c["b"]+s,e).then((function(t){return console.log("resource list"),console.log(t),t.data})).then((function(e){t.items=e,t.isLoad=!0,console.log(e)}));var a={category_id:this.$route.params.id.toString()};l.a.post(c["b"]+"getCategoryByID/",a).then((function(t){return console.log("resource list"),console.log(t),t.data})).then((function(e){t.title=e.name}))},searchResource:function(t){},changeDisplayMode:function(t){this.displayMode=t},changePageSize:function(t){this.page=1,this.perPage=t},changeOrderBy:function(t){this.sort=t},searchChange:function(t){var e=this;console.log("searchResource"),console.log(t);var s={text:t,categoryID:this.$route.params.id,personId:null};null!=this.currentUser&&(s.personId=this.currentUser.id),l.a.post(c["b"]+"searchResource/",s).then((function(t){return console.log("search resource"),console.log(t),t.data})).then((function(t){e.items=t,console.log(e.items),console.log(t)}))},selectAll:function(t){this.selectedItems.length>=this.items.length?t&&(this.selectedItems=[]):this.selectedItems=this.items.map((function(t){return t.id}))},keymap:function(t){switch(t.srcKey){case"select":this.selectAll(!1);break;case"undo":this.selectedItems=[];break}},getIndex:function(t,e,s){for(var a=0;a<e.length;a++)if(e[a][s]===t)return a;return-1},toggleItem:function(t,e){if(t.shiftKey&&this.selectedItems.length>0){var s,a=this.items,n=this.getIndex(e,a,"id"),i=this.getIndex(this.selectedItems[this.selectedItems.length-1],a,"id");a=a.slice(Math.min(n,i),Math.max(n,i)+1),(s=this.selectedItems).push.apply(s,Object(o["a"])(a.map((function(t){return t.id}))))}else this.selectedItems.includes(e)?this.selectedItems=this.selectedItems.filter((function(t){return t!==e})):this.selectedItems.push(e)},handleContextMenu:function(t){this.selectedItems.includes(t.key)||(this.selectedItems=[t.key])},onContextMenuAction:function(t){console.log("context menu item clicked - "+t+": ",this.selectedItems)},changePage:function(t){this.page=t}},computed:Object(i["a"])(Object(i["a"])({},Object(_["c"])({currentUser:"currentUser",menuType:"getMenuType",menuClickCount:"getMenuClickCount",selectedMenuHasSubItems:"getSelectedMenuHasSubItems"})),{},{isSelectedAll:function(){return this.selectedItems.length>=this.items.length},isAnyItemSelected:function(){return this.selectedItems.length>0&&this.selectedItems.length<this.items.length},apiUrl:function(){return"".concat(this.apiBase,"?sort=").concat(this.sort.column,"&page=").concat(this.page,"&per_page=").concat(this.perPage,"&search=").concat(this.search)}}),watch:{search:function(){this.page=1},apiUrl:function(){this.loadItems()}},mounted:function(){this.loadItems()}},dt=ut,mt=Object(C["a"])(dt,a,n,!1,null,null,null);e["default"]=mt.exports},af03:function(t,e,s){var a=s("d039");t.exports=function(t){return a((function(){var e=""[t]('"');return e!==e.toLowerCase()||e.split('"').length>3}))}},f7d9:function(t,e,s){"use strict";s.d(e,"a",(function(){return l})),s.d(e,"e",(function(){return g})),s.d(e,"b",(function(){return b})),s.d(e,"c",(function(){return k})),s.d(e,"d",(function(){return A}));var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 19 19"}},[s("path",{staticClass:"view-icon-svg",attrs:{d:"M17.5,3H.5a.5.5,0,0,1,0-1h17a.5.5,0,0,1,0,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M17.5,10H.5a.5.5,0,0,1,0-1h17a.5.5,0,0,1,0,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M17.5,17H.5a.5.5,0,0,1,0-1h17a.5.5,0,0,1,0,1Z"}})])},n=[],i=s("2877"),o={},r=Object(i["a"])(o,a,n,!1,null,null,null),l=r.exports,c=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 19 19"}},[s("path",{staticClass:"view-icon-svg",attrs:{d:"M17.5,3H6.5a.5.5,0,0,1,0-1h11a.5.5,0,0,1,0,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M3,2V3H1V2H3m.12-1H.88A.87.87,0,0,0,0,1.88V3.12A.87.87,0,0,0,.88,4H3.12A.87.87,0,0,0,4,3.12V1.88A.87.87,0,0,0,3.12,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M3,9v1H1V9H3m.12-1H.88A.87.87,0,0,0,0,8.88v1.24A.87.87,0,0,0,.88,11H3.12A.87.87,0,0,0,4,10.12V8.88A.87.87,0,0,0,3.12,8Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M3,16v1H1V16H3m.12-1H.88a.87.87,0,0,0-.88.88v1.24A.87.87,0,0,0,.88,18H3.12A.87.87,0,0,0,4,17.12V15.88A.87.87,0,0,0,3.12,15Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M17.5,10H6.5a.5.5,0,0,1,0-1h11a.5.5,0,0,1,0,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M17.5,17H6.5a.5.5,0,0,1,0-1h11a.5.5,0,0,1,0,1Z"}})])},u=[],d={},m=Object(i["a"])(d,c,u,!1,null,null,null),g=m.exports,p=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 19 19"}},[s("path",{staticClass:"view-icon-svg",attrs:{d:"M7,2V8H1V2H7m.12-1H.88A.87.87,0,0,0,0,1.88V8.12A.87.87,0,0,0,.88,9H7.12A.87.87,0,0,0,8,8.12V1.88A.87.87,0,0,0,7.12,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M17,2V8H11V2h6m.12-1H10.88a.87.87,0,0,0-.88.88V8.12a.87.87,0,0,0,.88.88h6.24A.87.87,0,0,0,18,8.12V1.88A.87.87,0,0,0,17.12,1Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M7,12v6H1V12H7m.12-1H.88a.87.87,0,0,0-.88.88v6.24A.87.87,0,0,0,.88,19H7.12A.87.87,0,0,0,8,18.12V11.88A.87.87,0,0,0,7.12,11Z"}}),t._v(" "),s("path",{staticClass:"view-icon-svg",attrs:{d:"M17,12v6H11V12h6m.12-1H10.88a.87.87,0,0,0-.88.88v6.24a.87.87,0,0,0,.88.88h6.24a.87.87,0,0,0,.88-.88V11.88a.87.87,0,0,0-.88-.88Z"}})])},h=[],f={},v=Object(i["a"])(f,p,h,!1,null,null,null),b=v.exports,x=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"text-center"},[s("svg",{staticClass:"main",attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 9 17"}},[s("rect",{attrs:{x:"0.48",y:"0.5",width:"7",height:"1"}}),t._v(" "),s("rect",{attrs:{x:"0.48",y:"7.5",width:"7",height:"1"}}),t._v(" "),s("rect",{attrs:{x:"0.48",y:"15.5",width:"7",height:"1"}})]),t._v(" "),s("svg",{staticClass:"sub",attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 18 17"}},[s("rect",{attrs:{x:"1.56",y:"0.5",width:"16",height:"1"}}),t._v(" "),s("rect",{attrs:{x:"1.56",y:"7.5",width:"16",height:"1"}}),t._v(" "),s("rect",{attrs:{x:"1.56",y:"15.5",width:"16",height:"1"}})])])},_=[],y={},w=Object(i["a"])(y,x,_,!1,null,null,null),k=w.exports,C=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 26 17"}},[s("rect",{attrs:{x:"0.5",y:"0.5",width:"25",height:"1"}}),t._v(" "),s("rect",{attrs:{x:"0.5",y:"7.5",width:"25",height:"1"}}),t._v(" "),s("rect",{attrs:{x:"0.5",y:"15.5",width:"25",height:"1"}})])},I=[],M={},O=Object(i["a"])(M,C,I,!1,null,null,null),A=O.exports},f8b6:function(t,e,s){"use strict";var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("b-card",{directives:[{name:"b-hover",rawName:"v-b-hover",value:t.handleHover,expression:"handleHover"}],attrs:{"no-body":""}},[s("router-link",{attrs:{to:"/app/resourceDetail/"+t.data.resource_id}},[s("img",{staticClass:"card-img-top",attrs:{src:"https://i.pcmag.com/imagery/articles/0270lteaknt7h4pBahOR4az-40..v1580751227.jpg",alt:t.data.title,width:"253",height:"202"}}),t._v(" "),s("b-badge",{staticClass:"position-absolute badge-top-left",attrs:{pill:"",variant:"primary"}},[s("i",{staticClass:"fa fa-thumbs-up fa-2x"},[t._v(" "+t._s(t.data.likeCount))])])],1),t._v(" "),s("a",{staticClass:"btn btn-primary",staticStyle:{"border-radius":"0px 0px 10px 10px"},attrs:{href:t.data.link}},[t._v("Visit tutorial")]),t._v(" "),s("b-card-body",[s("router-link",{attrs:{to:"/app/resourceDetail/"+t.data.resource_id}},[s("b-row",[s("b-colxx",{staticClass:"mb-3",attrs:{xxs:"12"}},[s("h6",{staticClass:"mb-4 card-subtitle"},[t._v(t._s(t.data.title))]),t._v(" "),t._l(t.data.tags,(function(e,a){return t.isHovered?t._e():s("b-badge",{key:a,staticClass:"mb-1 mr-1",attrs:{pill:"",variant:"outline-secondary"}},[t._v(t._s(e.title))])}))],2)],1)],1),t._v(" "),t.isHovered?s("b-row",[s("b-colxx",{attrs:{lg:"6"}},[0==t.data.isliked?s("b-button",{staticClass:"btn  btn-block  default text-center rounded",attrs:{variant:"primary"},on:{click:function(e){return t.like()}}},[s("i",{staticClass:"fa fa-thumbs-up fa-lg"})]):s("b-button",{staticClass:"btn  btn-block  default text-center rounded",attrs:{variant:"outline-primary"},on:{click:function(e){return t.unlike()}}},[s("i",{staticClass:"fa fa-thumbs-up fa-lg"})])],1),t._v(" "),s("b-colxx",{attrs:{lg:"6"}},[0==t.data.isbookmark?s("b-button",{staticClass:"btn  btn-block  default text-center rounded",attrs:{variant:"primary"},on:{click:function(e){return t.bookmark()}}},[s("i",{staticClass:"fa fa-bookmark fa-lg"})]):s("b-button",{staticClass:"btn  btn-block  default text-center rounded",attrs:{variant:"outline-primary"},on:{click:function(e){return t.deleteBookmark()}}},[s("i",{staticClass:"fa fa-bookmark fa-lg"})])],1)],1):t._e()],1)],1)},n=[],i=(s("d3b7"),s("25f0"),s("5530")),o=s("a9c6"),r=s("2f62"),l=s("bc3a"),c=s.n(l),u=s("2b47"),d={data:function(){return{isHovered:!1}},props:["data","selectedItems","loadItems"],components:{stars:o["a"]},computed:Object(i["a"])({},Object(r["c"])({currentUser:"currentUser",menuType:"getMenuType",menuClickCount:"getMenuClickCount",selectedMenuHasSubItems:"getSelectedMenuHasSubItems"})),methods:{handleHover:function(t){this.isHovered=t},bookmark:function(){var t=this;null==this.currentUser&&alert("You have to login for this feature"),console.log("add bookmark");var e={person_id:this.currentUser.id,resource_id:this.data.resource_id};c.a.post(u["b"]+"addBookmark/",e).then((function(e){return console.log("bookmark"),t.loadItems(),console.log(e),e.data}))},like:function(){var t=this;null==this.currentUser&&alert("You have to login for this feature");var e={pers:this.currentUser.id.toString(),resc:this.data.resource_id.toString()};c.a.post(u["b"]+"createLike/",e).then((function(e){return console.log("bookmark"),t.loadItems(),console.log(e),e.data}))},unlike:function(){var t=this,e={person_id:this.currentUser.id.toString(),resource_id:this.data.resource_id.toString()};c.a.post(u["b"]+"deleteLike/",e).then((function(e){return console.log("bookmark"),t.loadItems(),console.log(e),e.data}))},deleteBookmark:function(){var t=this;console.log("delete bookmark");var e={person_id:this.currentUser.id,resource_id:this.data.resource_id};c.a.post(u["b"]+"deleteBookmark/",e).then((function(e){return console.log("bookmark"),t.loadItems(),console.log(e),e.data}))}}},m=d,g=s("2877"),p=Object(g["a"])(m,a,n,!1,null,null,null);e["a"]=p.exports}}]);