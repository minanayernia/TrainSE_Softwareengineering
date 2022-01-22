<template>
<b-row>
    <b-colxx xxs="12">
        <b-row >
            <b-colxx xxs="12" lg="4" class="mb-4 col-left " >
                <div class="sticky-top">
                <b-card no-body class="mb-4 " >
                    <div class="position-absolute card-top-buttons">
                        <b-button variant="outline-white" class="icon-button">
                            <i class="simple-icon-pencil" />
                        </b-button>
                        
                    </div>
                    
                    <single-lightbox thumb="/assets/img/profiles/1.jpg" large="/assets/img/profiles/1.jpg" class-name="card-img-top" />
                    
                    <b-card-body>
                        <p class="text-muted text-small mb-2">{{$t('User Name')}}</p>
                        <p class="mb-3">
                            {{data.username}}
                        </p>
                        <p class="text-muted text-small mb-2">{{$t('menu.about')}}</p>
                        <p class="mb-3">
                            {{data.about}}
                        </p>
                        <p class="text-muted text-small mb-2">{{$t('pages.location')}}</p>
                        <p class="mb-3">{{data.location}}</p>
                                        
                        <p class="text-muted text-small mb-2">Email Address</p>
                        <p class="mb-3">{{data.email}}</p>

                        <b-row>                   
                    <div class="top-right-button-container">
                    <b-button
                    v-b-modal.modalright
                    variant="primary"
                    size="lg"
                    
                    class="btn btn-default btn-lg btn-block"
                    style="border-radius: 10px 10px 10px 10px; width: 413px;"
                    Large button
                    >{{ $t('Edit') }}</b-button>

                </div>
                <edit-new-modal :loadProfile="loadProfile" :id="currentUser.id" ></edit-new-modal>
                </b-row>
                    </b-card-body>
                    
                    
                </b-card>
                </div>
                
            </b-colxx>
            

            
                
            <b-colxx xxs="12" lg="8" class="mb-4 col-right" >

                <b-tabs nav-class="separator-tabs ml-0 mb-5" content-class="tab-content" :no-fade="true">
                
                <b-tab :title="$t('BOOKMARK')">
                    <b-row>
                        <b-colxx v-for="(item,itemIndex) in bookmarkedList" xxs="12" lg="6" xl="4" class="mb-4" :key="`product_${itemIndex}`">
                            <image-list-item
                                :key="item.resource_id"
                                :data="item"
                                :selected-items="selectedItems"
                                @toggle-item="toggleItem"
                                :loadItems="loadProfile"
                                />
                        </b-colxx>
                    
                    </b-row>
                </b-tab>

                <b-tab :title="$t('SUBMITED')">
                    <b-row>
                        <b-colxx v-for="(item,itemIndex) in submittedList" xxs="12" lg="6" xl="4" class="mb-4" :key="`product_${itemIndex}`">
                            <image-list-item
                                :key="item.resource_id"
                                :data="item"
                                :selected-items="selectedItems"
                                @toggle-item="toggleItem"
                                @loadItems="loadProfile"
                                />
                        </b-colxx>
                    
                    </b-row>
                </b-tab>
                <b-tab :title="$t('LIKED')">
                    <b-row>
                        <b-colxx v-for="(item,itemIndex) in likedList" xxs="12" lg="6" xl="4" class="mb-4" :key="`product_${itemIndex}`">
                            <image-list-item
                                :key="item.resource_id"
                                :data="item"
                                :selected-items="selectedItems"
                                @toggle-item="toggleItem"
                                :loadItems="loadProfile"
                                />
                        </b-colxx>
                    
                    </b-row>
                </b-tab>

                </b-tabs>
            </b-colxx>

        </b-row>

    </b-colxx>
</b-row>
</template>

<script>
import SingleLightbox from '../../../../containers/pages/SingleLightbox';
import RecentPost from '../../../../components/Common/RecentPost';
import UserCardBasic from "../../../../components/Cards/UserCardBasic";
import ImageListItem from "../../../../components/Listing/ImageListItem";

import { mapGetters, mapMutations, mapActions } from "vuex";


import produtcs from '../../../../data/products'
import recentPosts from "../../../../data/recentPosts";
import followers from "../../../../data/follow";
import { apiUrl ,api } from "../../../../constants/config";
import axios from "axios";
import EditNewModal from "../../../../containers/pages/EditNewModal";

export default {
    components: {
        'single-lightbox': SingleLightbox,
        'recent-post': RecentPost,
        'user-card-basic': UserCardBasic,
        "edit-new-modal": EditNewModal,
        "image-list-item": ImageListItem,
        
    },
    props: ["displayMode",
    "selectedItems",
    "toggleItem"],
    data() {
        return {
            data:{},
            bookmarkedList:{},
            submittedList:{},
            likedList:{},
            produtcs: produtcs.slice(0, 15),
            recentPosts,
            followers
        }
    },
    methods: {
        toggleItem(event, itemId) {
            this.$emit('toggle-item', event, itemId)
        },
        loadProfile(){
            console.log("Loading Profile");
            console.log(this.$route.params.id);

            this.loadBookMarks();
            this.loadSubmitted();
            this.loadLiked();
            const user = {
                id:this.currentUser.id,
            };
            axios
                .post(api+"showProfile/",user)
                .then(response => {
                console.log("user");
                console.log(response);
                return response.data;
                })
                .then(res => {
                    this.data=res;
                    console.log(res);
                });
        },
        loadBookMarks(){
            console.log("Loading bookmark");
            
        const bookmark = {
            id:this.currentUser.id,
            };
            axios
                .post(api+"BookmarkedList/",bookmark)
                .then(response => {
                console.log("bookmark");
                console.log(response);
                return response.data;
                })
                .then(res => {
                    this.bookmarkedList=res;
                    console.log(res);
                });
        },
        loadSubmitted(){
            console.log("Loading submitted");
            
        const submit = {
        id:this.currentUser.id,
        };
        axios
        .post(api+"submittedResourceList/",submit)
        .then(response => {
          console.log("bookmark");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.submittedList=res;
            console.log(res);
        });
        },
        loadLiked(){
            console.log("Loading liked");
            
        const like = {
        id:this.currentUser.id,
      };
      axios
        .post(api+"likeResourseList/",like)
        .then(response => {
          console.log("bookmark");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.likedList=res;
            console.log(res);
        });
        },
    },
    computed: {
    ...mapGetters({
      currentUser: "currentUser",
      menuType: "getMenuType",
      menuClickCount: "getMenuClickCount",
      selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    })
  },
    mounted() {
        setTimeout(() => {
      this.isLoad = true;
    }, 50);
    this.loadProfile();
    this.loadBookMarks();
    this.loadSubmitted();
    this.loadLiked();
    }
}
</script>
