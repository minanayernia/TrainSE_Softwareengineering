<template>
  <b-row class="h-100">
    <b-colxx
      xxs="12"
      md="10"
      lg="7"
      xxl="6"
      class="mx-auto my-auto"
      style="margin:5em auto !important;"
    >
      <b-card class="auth-card" no-body>
        <div class="form-side" style="width:100%;">
          <h6 class="mb-4">Login</h6>

          <b-form
            @submit.prevent="formSubmit"
            class="av-tooltip tooltip-label-bottom"
          >
            <b-form-group label="user-name" class="has-float-label mb-4">
              <b-form-input
                type="text"
                v-model="$v.form.username.$model"
                :state="!$v.form.username.$error"
              />
              <b-form-invalid-feedback v-if="!$v.form.username.required"
                >please enter your username.</b-form-invalid-feedback
              >
            </b-form-group>

            <b-form-group
              :label="$t('user.password')"
              class="has-float-label mb-4"
            >
              <b-form-input
                type="password"
                v-model="$v.form.password.$model"
                :state="!$v.form.password.$error"
              />
              <b-form-invalid-feedback v-if="!$v.form.password.required"
                >Please enter your password</b-form-invalid-feedback
              >
            </b-form-group>
            <div class="d-flex justify-content-between align-items-center">
              <router-link tag="a" to="/user/register">Register</router-link>
              <b-button type="submit" variant="primary" size="lg">
                <span class="label">Login</span>
              </b-button>
            </div>
          </b-form>
        </div>
      </b-card>
    </b-colxx>
  </b-row>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { validationMixin } from "vuelidate";
import { adminRoot } from "../../constants/config";
const {
  required,
  maxLength,
  minLength,
  email
} = require("vuelidate/lib/validators");

export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  mixins: [validationMixin],
  validations: {
    form: {
      password: {
        required,
        maxLength: maxLength(16),
        minLength: minLength(4)
      },
      username: {
        required,
        maxLength: maxLength(30)
      }
    }
  },
  computed: {
    ...mapGetters(["currentUser", "processing", "loginError"])
  },
  methods: {
    ...mapActions(["login"]),
    formSubmit() {
      console.log("login");

      this.login({
        username: this.form.username,
        password: this.form.password
      });
    }
  },
  watch: {
    currentUser(val) {
      if (val && val.uid && val.uid.length > 0) {
        setTimeout(() => {
          this.$router.push(adminRoot);
        }, 200);
      }
    },
    loginError(val) {
      if (val != null) {
        this.$notify("error", "Login Error", val, {
          duration: 3000,
          permanent: false
        });
      }
    }
  }
};
</script>
