/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ZonesTenantIdQuestions = function () {
    /*
        @params obj 'data params'
            tenant_id   'string' tenant id in path
            content   'string' 
            is_public   'boolean' 
            images   'array' 
            comment   'string' 
            
        @success
            status 201    type:object
            status   'ref' 
            asker   'ref' 
            offer   'ref' 
            date_updated   'ref' 
            respondent_id   'ref' 
            content   'ref' 
            date_created   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/zones/" + obj.tenant_id + "/questions",
            method: "POST",
            data: {
                content: obj.content,
                is_public: obj.is_public,
                images: obj.images,
                comment: obj.comment
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    ZonesTenantIdQuestions: new ZonesTenantIdQuestions
};