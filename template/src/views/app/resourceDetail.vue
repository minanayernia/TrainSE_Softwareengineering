<template>
  <div>
    <b-row>
      <b-colxx xxs="12">
        <h1>{{data.title}}</h1>
        <div class="top-right-button-container">
          <b-dropdown
            v-if="currentUser!=null"
            id="ddown5"
            :text="$t('pages.actions')"
            size="lg"
            variant="outline-primary"
            class="top-right-button top-right-button-single"
            no-fade="true"
          >
            <b-dropdown-item
            v-if="currentUser.username==data.submitter"
            v-b-modal.edit
            
            >{{ $t('EDIT') }}</b-dropdown-item>

            <b-dropdown-item
            @click="report($route.params.id)"
            >{{ $t('REPORT') }}</b-dropdown-item>

            <edit-resource @update="loadResources" :id="this.$route.params.id" :categoryId="data.category" ></edit-resource>

          </b-dropdown>
        </div>
        <b-tabs nav-class="separator-tabs ml-0 mb-5" content-class="tab-content" :no-fade="true">
            <b-row>
              <b-colxx xxs="12" lg="4" class="mb-4">
                <b-card class="mb-4" no-body>
                  <img src="https://i.pcmag.com/imagery/articles/0270lteaknt7h4pBahOR4az-40..v1580751227.jpg" alt="Detail" class="card-img-top" />
                  <b-button :href="data.link" variant="primary" style="border-radius: 0px 0px 10px 10px;">Visit tutorial</b-button>
                  <b-card-body>
                    <p class="text-muted text-small mb-2">{{ $t('pages.description') }}</p>
                    <p class="mb-3">{{data.description}}</p>
                    <p class="text-muted text-small mb-2">{{ $t('todo.labels') }}</p>
                    <div class="mb-3">
                      <p class="d-sm-inline-block mb-1">
                        <b-badge v-for="(tag,index) in data.tags" :key="index" pill variant="outline-secondary" class="mb-1 mr-1">{{tag.title}}</b-badge>
                      </p>
                    </div>

                    <b-card class="mb-4 d-flex flex-row" no-body>
              <router-link to="?" class="d-flex">
                <div
                  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDqZLNNtpV-cNZfqbScWb3_Ny0C15rPO9mgg&usqp=CAU"
                  class="align-self-center list-thumbnail-letters rounded-circle m-4 small"
                >S</div>
              </router-link>
              <div class="d-flex flex-grow-1 min-width-zero">
                <div
                  class="pl-0 align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero"
                >
                  <div class="min-width-zero">
                    <router-link to="?">
                      <h6 class="mb-1 card-subtitle truncate">{{data.submitter}}</h6>
                    </router-link>
                    <p class="text-muted text-small mb-2">Submitter</p>
                  </div>
                </div>
              </div>
            </b-card>
                    
                  </b-card-body>
                </b-card>
                
              </b-colxx>
              <b-colxx xxs="12" lg="8">
              <icon-cards-carousel :data="data" :VideoQuality="VideoQuality" :ContentQuality="ContentQuality" :CourseDepth="CourseDepth" :CoursePace="CoursePace" :QualifiedInstructor="QualifiedInstructor"></icon-cards-carousel>
                  
                <b-card class="mb-4" :title="$t('pages.comments')">
                  <comment-item
                    v-for="(comment,index) in data.comment"
                    :key="index"
                    :data="comment"
                    :replyComment="replyComment"
                    :likeComment="likeComment"
                    detail-path="#"
                  />
                  <b-input-group class="comment-contaiener">
                    <b-input v-model="comment_txt" :placeholder="$t('pages.addComment')" />
                    <template v-slot:append>
                      <b-button variant="primary" @click="send()">
                        <span class="d-inline-block">{{$t('pages.send')}}</span>
                        <i class="simple-icon-arrow-right ml-2"></i>
                      </b-button>
                    </template>
                </b-input-group>
                </b-card>
              </b-colxx>
            </b-row>
          </b-tab>

        </b-tabs>
      </b-colxx>
    </b-row>
  </div>
</template>

<script>
import CommentItem from "../../components/Listing/CommentItem";
import { apiUrl ,api } from "../../constants/config";
import axios from "axios";
import EditResource from "../../containers/pages/EditResource";
import { mapGetters, mapMutations, mapActions } from "vuex";
import IconCardsCarousel from "../../containers/dashboards/IconCardsCarousel";

export default {
  components: {
    stars: Stars,
    "comment-item": CommentItem,
    "edit-resource": EditResource,
    "icon-cards-carousel": IconCardsCarousel,

  },
  data() {
    return {
      data:{},
      comment_txt:"",
      isLoad: false,
      repleyID:null,
    };
  },
  computed: {
    ...mapGetters({
      currentUser: "currentUser",
      menuType: "getMenuType",
      menuClickCount: "getMenuClickCount",
      selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    })
  },
  methods: {
    VideoQuality(){
        if(this.currentUser==null){
          alert("You have to login for this feature");
        }
        console.log("khoboibgoigboug")
        const data = {
        pers:this.currentUser.id.toString(),
        resc:this.$route.params.id.toString(),
      };
      axios
        .post(api+"VideoQuality/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
            this.loadResources();
            console.log(res);
        });
    },
    ContentQuality(){
        if(this.currentUser==null){
          alert("You have to login for this feature");
        }
        console.log("khoboibgoigboug")
        const data = {
        pers:this.currentUser.id.toString(),
        resc:this.$route.params.id.toString(),
      };
      axios
        .post(api+"ContentQuality/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
            this.loadResources();
            console.log(res);
        });
    },
    CourseDepth(){
        if(this.currentUser==null){
          alert("You have to login for this feature");
        }
        console.log("khoboibgoigboug")
        const data = {
        pers:this.currentUser.id.toString(),
        resc:this.$route.params.id.toString(),
      };
      axios
        .post(api+"CourseDepth/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
            this.loadResources();
            console.log(res);
        });
    },
    CoursePace(){
        if(this.currentUser==null){
          alert("You have to login for this feature");
        }
        console.log("khoboibgoigboug")
        const data = {
        pers:this.currentUser.id.toString(),
        resc:this.$route.params.id.toString(),
      };
      axios
        .post(api+"CoursePace/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
            this.loadResources();
            console.log(res);
        });
    },
    QualifiedInstructor(){
        if(this.currentUser==null){
          alert("You have to login for this feature");
        }
        console.log("khoboibgoigboug")
        const data = {
        pers:this.currentUser.id.toString(),
        resc:this.$route.params.id.toString(),
      };
      axios
        .post(api+"QualifiedInstructor/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
            this.loadResources();
            console.log(res);
        });
    },
    report(id){
      if(this.currentUser==null){
        alert("You have to login for this feature");
      }
      console.log("report")
      console.log(this.currentUser)
      const data = {
        person_id:this.currentUser.id,
        resource_id:this.$route.params.id,
      };
      axios
        .post(api+"reportResource/",data)
        .then(response => {

          return response.data;
        })
        .then(res => {
            if(res.status==500) {
              alert("you report this item before")
            }
            else{
              alert("report done")
            }
            this.loadResources();
            
        });
    },
    likeComment (id){
      if(this.currentUser==null){
        alert("You have to login for this feature");
      }
      const like_data = {
        pers:this.currentUser.id.toString(),
        comment:id.toString(),
      };
      axios
        .post(api+"likecomment/",like_data)
        .then(response => {

          return response.data;
        })
        .then(res => {
            this.loadResources();
            console.log(res);
        });
    },
    send(){
      if(this.currentUser==null){
        alert("You have to login for this feature");
      }
      const comment = {
        pers:this.currentUser.id,
        resc:this.$route.params.id,
        text:this.comment_txt,
        reply_comment:this.repleyID,

      };
      axios
        .post(api+"createcomment/",comment)
        .then(response => {
          return response.data;
        })
        .then(res => {
          this.loadResources();
          this.comment_txt="";
            console.log(res);
        });
    },
    replyComment(id){

      const data = {
        person_id:this.currentUser.id,
        comment_id:id,
      };
      axios
        .post(api+"reportComment/",data)
        .then(response => {

          return response.data;
        })
        .then(res => {
            if(res.status==500) {
              alert("you report this item before")
            }
            else{
              alert("report done")
            }
        });
    },
    loadResources(){
      console.log("Loading single resouce");
      console.log(this.$route.params.id);
      const resource = {
        resourceId:this.$route.params.id,
      };
      axios
        .post(api+"singleResource/",resource)
        .then(response => {
          console.log("res list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.data=res;
            console.log(res);
        });
    }
  },
  mounted() {
    setTimeout(() => {
      this.isLoad = true;
    }, 50);
    this.loadResources();
  }
};
</script>
