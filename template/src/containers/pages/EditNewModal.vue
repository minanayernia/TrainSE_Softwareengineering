
<template>
  <b-modal
    id="modalright"
    ref="modalright"
    title="Edit Profile"
    size="md"
    hide-footer
  >
    <b-card no-body>
      <b-card-body>

        <b-form>
          <b-form-group label="Name:">
            <b-form-input v-model="newItem.username" placeholder="UserName"/>
          </b-form-group>
          <b-form-group label="About:">
            <b-form-input v-model="newItem.about" placeholder="About"/>
          </b-form-group>
          <b-form-group label="Location:">
            <b-form-input v-model="newItem.location" placeholder="Location"/>
          </b-form-group>

          <b-form-group label="Email:">
            <b-form-input v-model="newItem.email" placeholder="Email"/>
          </b-form-group>
        </b-form>
            <button
                type="button"
                class="btn btn-primary"
                @click="addNewItem"
              >
                save
              </button>
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
  props: ["categoryID","loadProfile","data"],
  data() {
    return {

      newItem: {
        
      },

      error: "",

     

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
    loadProfile(){
        console.log("Loading Profile");
        console.log(this.$route.params.id);

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
                this.newItem=res;
                console.log(res);
            });
    },
    addNewItem() {
      const user = {
        id:this.currentUser.id,
        username: this.newItem.username,
        about: this.newItem.about,
        email: this.newItem.email,
        password: this.newItem.password,
        location: this.newItem.location,
      };
      axios
        .post(`${api}updatePerson/`, user)
        .then((response) => {
          return response.data;
        })
        .then((res) => {
          console.log("edit profile")
          console.log(res);
          this.loadProfile();
          this.hideModal("modalright");
          this.newItem.UserName = "";
          this.newItem.About = "";
          this.newItem.Email ="";
          this.newItem.Location = "";
          this.newItem.PassWord = "";
          

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
    this.loadProfile();
  }
};
</script>

