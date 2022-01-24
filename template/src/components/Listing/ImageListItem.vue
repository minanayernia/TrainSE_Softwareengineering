<template>

    <b-card  no-body v-b-hover="handleHover">
        <router-link :to="`/app/pages/product/details-alt/${data.resource_id}`" >

        <img src="https://i.pcmag.com/imagery/articles/0270lteaknt7h4pBahOR4az-40..v1580751227.jpg" class="card-img-top" :alt="data.title"  width="253" height="202" />
        <b-badge pill variant="primary" class="position-absolute badge-top-left"><i class="fa fa-thumbs-up fa-2x"> {{data.likeCount}}</i></b-badge>
        </router-link> 

        <a class="btn btn-primary" :href="data.link" style="border-radius: 0px 0px 10px 10px;">Visit tutorial</a>

        <b-card-body>
          <router-link :to="`/app/pages/product/details-alt/${data.resource_id}`">
            <b-row>
                <b-colxx xxs="12" class="mb-3">
                    <h6 class="mb-4 card-subtitle">{{data.title}}</h6>
                    <b-badge v-if="!isHovered" v-for="(tag,index) in data.tags" :key="index" pill variant="outline-secondary" class="mb-1 mr-1">{{tag.title}}</b-badge>
                </b-colxx>
                    
            </b-row>
          </router-link>
            <b-row v-if="isHovered">
              <b-colxx  lg="6">
                <b-button  v-if="data.isliked == 0" variant="primary" class="btn  btn-block  default text-center rounded"  @click="like()"
                  ><i class="fa fa-thumbs-up fa-lg"></i></b-button>
                <b-button  v-else variant="outline-primary" class="btn  btn-block  default text-center rounded"  @click="unlike()"
                  ><i class="fa fa-thumbs-up fa-lg"></i></b-button>
              </b-colxx>
            <b-colxx  lg="6">
              <b-button v-if="data.isbookmark == 0" variant="primary" class="btn  btn-block  default text-center rounded" @click="bookmark()"
                ><i class="fa fa-bookmark fa-lg"></i></b-button
              >
              <b-button v-else variant="outline-primary" class="btn  btn-block  default text-center rounded" @click="deleteBookmark()"
                ><i class="fa fa-bookmark fa-lg"></i></b-button
              >
            </b-colxx>            
          </b-row>
        </b-card-body>
        
    </b-card>
</template>

<script>
import Stars from '../Common/Stars'
import { mapGetters, mapMutations, mapActions } from "vuex";
import axios from "axios";
import { apiUrl ,api } from "../../constants/config";

export default {
    data(){
        return{
            isHovered:false,
        };
        
    },

    props: ['data', 'selectedItems' , 'loadItems'],
    components: {
        'stars': Stars
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

        handleHover(hovered) {
            this.isHovered = hovered
        },
        bookmark(){
          if(this.currentUser==null){
            alert("You have to login for this feature");
          }
          console.log("add bookmark"); 
          const bookmark = {
          person_id:this.currentUser.id,
          resource_id: this.data.resource_id,
          };
        axios
          .post(api+"addBookmark/",bookmark)
          .then(response => {
            console.log("bookmark");
            this.loadItems();
            console.log(response);
            return response.data;
          });
        },
        like(){
          if(this.currentUser==null){
            alert("You have to login for this feature");
          }
          const like = {
          pers:this.currentUser.id.toString(),
          resc: this.data.resource_id.toString(),
          };
        axios
          .post(api+"createLike/",like)
          .then(response => {
            console.log("bookmark");
            this.loadItems();
            console.log(response);
            return response.data;
          });
        },
        unlike(){
          const like = {
          person_id:this.currentUser.id.toString(),
          resource_id: this.data.resource_id.toString(),
          };
        axios
          .post(api+"deleteLike/",like)
          .then(response => {
            console.log("bookmark");
            this.loadItems();
            console.log(response);
            return response.data;
          });
        },
        deleteBookmark(){
          console.log("delete bookmark"); 
          const bookmark = {
          person_id:this.currentUser.id,
          resource_id: this.data.resource_id,
          };
          axios
            .post(api+"deleteBookmark/",bookmark)
            .then(response => {
              console.log("bookmark");
              this.loadItems();
              console.log(response);
              return response.data;
            });
        }

    }
}
</script>
