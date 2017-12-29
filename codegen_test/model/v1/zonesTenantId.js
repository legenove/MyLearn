/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ZonesTenantId = function () {
    /*
        @params obj 'data params'
            tenant_id   'string' tenant id in path
            
        @success
            status 200    type:object
            has_comment   'boolean' 
            description   'string' 
            title   'string' 
            tenant_id   'string' 
            image   'string' 
            has_daily_qa   'boolean' 
            modules   'array' 
            has_respondents   'boolean' 
            share_description   'string' 
            share_title   'string' 
            image_href   'string' 
            has_rank   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/zones/" + obj.tenant_id + "",
            method: "GET",
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
    ZonesTenantId: new ZonesTenantId
};