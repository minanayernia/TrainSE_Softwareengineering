<template>

    <b-card  no-body>
            <router-link :to="`/app/pages/product/details-alt/${data.resource_id}`" >

            <img src="https://i.pcmag.com/imagery/articles/0270lteaknt7h4pBahOR4az-40..v1580751227.jpg" class="card-img-top" :alt="data.title"  width="253" height="202" />

            </router-link> 

            <a class="btn btn-primary" :href="data.link" style="border-radius: 0px 0px 10px 10px;">Visit tutorial</a>

            <b-button v-if="data.isbookmark == 0" :variant="data.statusColor"
            class="position-absolute badge-top-left"
             @click="bookmark()">
                        <i class="iconsminds-bookmark"></i>
                      </b-button>
            <b-button v-if="data.isbookmark == 1" variant="outline-secondary"
            class="position-absolute badge-top-left"
             @click="deleteBookmark()">
                        <i class="iconsminds-bookmark"></i>
                      </b-button>
        <router-link :to="`/app/pages/product/details-alt/${data.resource_id}`">
        <b-card-body>
            <b-row>
                <b-colxx xxs="10" class="mb-3">
                    <h6 class="mb-4 card-subtitle">{{data.title}}</h6>
                </b-colxx>
                <div class="mb-3">
                        <p class="d-sm-inline-block mb-1">
                        <b-badge v-for="(tag,index) in data.tags" :key="index" pill variant="outline-secondary" class="mb-1 mr-1">{{tag.title}}</b-badge>
                        </p>
                    </div>
            </b-row>
        </b-card-body>
        </router-link>
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
        toggleItem(event, itemId) {
            this.$emit('toggle-item', event, itemId)
        },

        bookmark(){
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
