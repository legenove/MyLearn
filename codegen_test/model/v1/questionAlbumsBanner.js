/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionAlbumsBanner = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:object
            album   'ref' banner如果是专辑，显示专辑信息和第一个问题
            question   'ref' banner如果是问题
            description   'string' 活动说明
            title   'string' banner的title
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/question_albums/banner",
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
    QuestionAlbumsBanner: new QuestionAlbumsBanner
};