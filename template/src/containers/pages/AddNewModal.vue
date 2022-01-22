
<template>
  <b-modal
    id="modalright"
    ref="modalright"
    title="Add New Resource"
    size="md"
    hide-footer
  >
    <b-card no-body>
      <b-card-body class="wizard wizard-default">
        <form-wizard :last-step-end="true">
          <tab
            name="Properties"
            :selected="true"
          >
            <div class="wizard-basic-step">
              <b-form>
                <b-form-group label="Title:">
                  <b-form-input v-model="newItem.title" placeholder="enter title of resource"/>
                </b-form-group>
                <b-form-group label="Link:">
                  <b-form-input v-model="newItem.link" placeholder="enter link to resource"/>
                </b-form-group>
                <b-form-group label="Description: (optional)">
                  <b-textarea v-model="newItem.description" :rows="4" :max-rows="2" placeholder="enter description of resource"/>
                </b-form-group>
    
              </b-form>
            </div>
          </tab>

         <tab
            name="tags"
            :selected="false"
          >
            <div class="wizard-basic-step">

              <div v-for="(filterItem,index) in filters" >
                <label >{{filterItem.title}}</label>
                <b-form-checkbox-group v-model="selectedFilters" stacked class="list-unstyled mb-4">
                  <b-form-checkbox  v-for="(tag, index) in filterItem.tags"  :name="filterItem.title" :value="tag.id">{{tag.title}}</b-form-checkbox>
                </b-form-checkbox-group>   
              </div>

              <div v-for="(filterItem,index) in subCategories" >
                <label >{{filterItem.title}}</label>
                <b-form-checkbox-group v-model="selectedsubCategories" stacked class="list-unstyled mb-4">
                  <b-form-checkbox  v-for="(tag, index) in filterItem.tags"  :name="filterItem.title" :value="tag.id">{{tag.title}}</b-form-checkbox>
                </b-form-checkbox-group>   
              </div>
            </div>
          </tab>

          <tab type="done">
            <div class="wizard-basic-step text-center">
              <h2 class="mb-2">Are you sure you want to submit this resource?</h2>
              <button
                type="button"
                class="btn btn-primary"
                @click="addNewItem"
              >
                submit
              </button>
            </div>
          </tab>
        </form-wizard>
      </b-card-body>
    </b-card>
  </b-modal>
</template>

<script>
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import Tab from "../../components/Form/Wizard/Tab";

import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

import VueDropzone from "vue2-dropzone";
import { mapGetters, mapMutations, mapActions } from "vuex";

import { quillEditor } from "vue-quill-editor";
import { apiUrl ,api } from "../../constants/config";
import axios from "axios";
import FormWizard from "../../components/Form/Wizard/FormWizard";

export default {
  components: {
    "v-select": vSelect,
    Tab,
    FormWizard,
    "vue-dropzone": VueDropzone,
  },
  props: ["categoryID"],
  data() {
    return {
      tags:[],
      filters:[],
      subCategories:[],
      filter:[],
      selectedFilters:[],
      selectedsubCategories:[],
      checkBoxTags: [
          { text: 'free', value: 1 },
          { text: 'paid', value: 2 },
          { text: 'beginner', value: 3 },
          { text: 'advanced', value: 4 }
        ],
      newItem: {
        title: "",
        link:"",
        description: "",
        tags:[],
      },

      error: "",

      mainImageDropzoneOptions: {
        url: `${apiUrl}/upload`,
        thumbnailHeight: 150,
        maxFilesize: 2,
        maxFiles: 1,
        acceptedFiles: "image/*",
        dictDefaultMessage: "drop image of tutorial in this box",
        previewTemplate: this.dropzoneTemplate(),
      }

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
    
    loadFilters(){
      console.log()

      axios
        .get(api+"ListTags/")
        .then(response => {
          console.log("tags list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.tags = res;
            for (var i = 0; i <res.length; i++) {
              if(!this.filter.includes(res[i].type)){
                this.filter.push(res[i].type);
              }
            }
            for (var j=0; j < this.filter.length; j++) {
              var temp=[];
              for (var i = 0; i <this.tags.length; i++) {
                if(this.filter[j]==this.tags[i].type){
                  temp.push(this.tags[i]);
                }
              }
              this.filters.push({title:this.filter[j],tags:temp})
            }
            console.log("filters")
            console.log(this.filters)
      });
    },

    loadSubCategory(){
      const data={
        categoryId:this.categoryID
      }

      axios
        .post(api+"subcategoryList/",data)
        .then(response => {
          return response.data;
        })
        .then(res => {
          this.subCategories.push({title:"cubcategory",tags:res})
          console.log(this.filters)
      });
    },
    addNewItem() {
      const resource = {
        submitter:this.currentUser.id,
        category:this.categoryID,
        title: this.newItem.title,
        link: this.newItem.link,
        description: this.newItem.description,
        tags: this.selectedFilters,
        subs: this.selectedsubCategories,
      };
      axios
        .post(`${api}createResource/`, resource)
        .then((response) => {
          return response.data;
        })
        .then((res) => {
          console.log("add new resource")
          console.log(res);
          this.hideModal("modalright");
          this.newItem.title = "";
          this.newItem.link = "";
          this.newItem.description ="";
          this.newItem.tags =[];
          this.$emit('update');
        });
    },

    hideModal(refname) {
      this.$refs[refname].hide();
    },

    dropzoneTemplate() {
      return `<div class="dz-preview dz-file-preview mb-3">
                <div class="d-flex flex-row "> 
                  <div class="p-0 w-30 position-relative">
                    <div class="dz-error-mark"><span><i></i>  </span></div>
                    <div class="dz-success-mark"><span><i></i></span></div>
                    <div class="preview-container">
                      <img data-dz-thumbnail class="img-thumbnail border-0" />
                      <i class="simple-icon-doc preview-icon"></i>
                    </div>
                  </div>
                  <div class="pl-3 pt-2 pr-2 pb-1 w-40 dz-details position-relative m-2">
                    <div> <span data-dz-name style="direction:ltr" /> </div>
                    <div class="text-primary text-extra-small" style="direction:ltr" data-dz-size /> </div>
                    <div class="dz-progress"><span class="dz-upload" data-dz-uploadprogress></span></div>
                    <div class="dz-error-message"><span data-dz-errormessage></span></div>
                  </div>
                  <a href="#" class="remove" data-dz-remove> <i class="glyph-icon simple-icon-trash"></i> </a>
                </div>
              </div>
        `;
    },

    mainImageUploadSuccess(file, response) {
      this.newItem.mainImage = response.url;
    },
    mainImageDeleteFile(file, error, xhr) {
      console.log(file);
      console.log(error);
      console.log(xhr);
    },
  },
  mounted() {
    this.loadSubCategory();
    this.loadFilters();
  }
};
</script>

