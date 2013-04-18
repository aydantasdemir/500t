function Voter () {

    this.set_vote_url = function(voteURL) {
        this.vote_url = voteURL;

        return this;
    };

    this.set_point_element = function(pointElement) {
        this.point_element = pointElement;

        return this;
    };

    this.vote = function() {
        var point_element = this.point_element;
        $.getJSON(this.vote_url, function(data) {
            if(data.status == 1) {
                $('#' + point_element).hide();
                $('#' + point_element).fadeIn('slow');
                $('#' + point_element).html(data.message + " puan");
            }
            else {
                alert(data.message);
            }
        });
    };

}

$(document).ready(function() {
    $('.iconic').click(function(e) {
        var voter = new Voter();
        voter.set_vote_url($(this).attr('href'));
        voter.set_point_element($(this).attr('point_element'));
        voter.vote();

        e.preventDefault();
    });
});